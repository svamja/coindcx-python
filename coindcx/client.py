"""
CoinDCX API Client

A unified client for accessing both public and authenticated CoinDCX API endpoints.
"""

import hmac
import hashlib
import json
import time
from typing import Dict, Optional, Any, Union
from urllib.parse import urljoin

import requests

from .exceptions import (
    CoinDCXAPIException,
    CoinDCXRequestException,
    CoinDCXAuthenticationException,
    CoinDCXRateLimitException,
)
from .enums import (
    API_BASE_URL,
    PUBLIC_BASE_URL,
    OrderSide,
    OrderType,
    FuturesOrderType,
    NotificationType,
    TimeInForce,
    FuturesMarginMode,
    PositionMarginType,
)
from .endpoints.market import MarketEndpoints
from .endpoints.spot import SpotEndpoints
from .endpoints.margin import MarginEndpoints
from .endpoints.futures import FuturesEndpoints


class Client:
    """
    CoinDCX API Client

    Handles both public and authenticated endpoints. Authentication is optional
    at initialization - if API key and secret are not provided, only public
    endpoints will be accessible.

    Args:
        api_key (str, optional): Your CoinDCX API key
        api_secret (str, optional): Your CoinDCX API secret
        base_url (str, optional): Override the default API base URL
        public_url (str, optional): Override the default public API base URL
        timeout (int, optional): Request timeout in seconds. Default: 30

    Example:
        # For public endpoints only
        client = Client()
        markets = client.get_markets()

        # For authenticated endpoints
        client = Client(api_key="your_key", api_secret="your_secret")
        balances = client.get_balances()
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        api_secret: Optional[str] = None,
        base_url: str = API_BASE_URL,
        public_url: str = PUBLIC_BASE_URL,
        timeout: int = 30,
    ):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url
        self.public_url = public_url
        self.timeout = timeout
        self.session = requests.Session()

        # Initialize endpoint modules
        self.market = MarketEndpoints(self._get)
        self.spot = SpotEndpoints(self._post)
        self.margin = MarginEndpoints(self._post)
        self.futures = FuturesEndpoints(self._get, self._post)

    def _generate_signature(self, payload: str) -> str:
        """
        Generate HMAC-SHA256 signature for authenticated requests

        Args:
            payload: JSON string of the request body

        Returns:
            Hexadecimal signature string
        """
        if not self.api_secret:
            raise CoinDCXAuthenticationException(
                "API secret is required for authenticated requests"
            )

        secret_bytes = bytes(self.api_secret, encoding='utf-8')
        signature = hmac.new(
            secret_bytes,
            payload.encode(),
            hashlib.sha256
        ).hexdigest()

        return signature

    def _get_timestamp(self) -> int:
        """
        Get current EPOCH timestamp in milliseconds

        Returns:
            Current timestamp in milliseconds
        """
        return int(round(time.time() * 1000))

    def _request(
        self,
        method: str,
        endpoint: str,
        authenticated: bool = False,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        use_public_url: bool = False,
    ) -> Any:
        """
        Internal method to make HTTP requests

        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path
            authenticated: Whether this is an authenticated request
            params: URL parameters for GET requests
            data: Request body for POST requests
            use_public_url: Use public URL instead of main API URL

        Returns:
            JSON response from the API

        Raises:
            CoinDCXAuthenticationException: If authentication is required but credentials not provided
            CoinDCXRateLimitException: If rate limit is exceeded
            CoinDCXAPIException: For API errors
            CoinDCXRequestException: For network/request errors
        """
        # Check authentication
        if authenticated and (not self.api_key or not self.api_secret):
            raise CoinDCXAuthenticationException(
                "API key and secret are required for authenticated endpoints. "
                "Initialize the client with: Client(api_key='...', api_secret='...')"
            )

        # Build URL
        base = self.public_url if use_public_url else self.base_url
        url = urljoin(base, endpoint)

        # Prepare headers
        headers = {
            'Content-Type': 'application/json',
        }

        # Handle authenticated requests
        if authenticated:
            # Add timestamp to data if not present
            if data is None:
                data = {}

            if 'timestamp' not in data:
                data['timestamp'] = self._get_timestamp()

            # Generate signature
            json_body = json.dumps(data, separators=(',', ':'))
            signature = self._generate_signature(json_body)

            # Add authentication headers
            headers['X-AUTH-APIKEY'] = self.api_key
            headers['X-AUTH-SIGNATURE'] = signature

            # Make request
            try:
                response = self.session.request(
                    method=method,
                    url=url,
                    headers=headers,
                    data=json_body,
                    timeout=self.timeout,
                )
            except requests.exceptions.RequestException as e:
                raise CoinDCXRequestException(f"Request failed: {str(e)}")
        else:
            # Public request
            try:
                response = self.session.request(
                    method=method,
                    url=url,
                    headers=headers,
                    params=params,
                    timeout=self.timeout,
                )
            except requests.exceptions.RequestException as e:
                raise CoinDCXRequestException(f"Request failed: {str(e)}")

        # Handle response
        return self._handle_response(response)

    def _handle_response(self, response: requests.Response) -> Any:
        """
        Handle API response and raise appropriate exceptions

        Args:
            response: requests Response object

        Returns:
            Parsed JSON response

        Raises:
            CoinDCXRateLimitException: If rate limit exceeded
            CoinDCXAPIException: For other API errors
        """
        # Check for rate limiting
        if response.status_code == 429:
            raise CoinDCXRateLimitException(
                "Rate limit exceeded",
                status_code=response.status_code,
                response=response.text,
            )

        # Try to parse JSON response
        try:
            json_response = response.json()
        except ValueError:
            # Not JSON response
            if not response.ok:
                raise CoinDCXAPIException(
                    f"HTTP {response.status_code}: {response.text}",
                    status_code=response.status_code,
                    response=response.text,
                )
            return response.text

        # Check for API errors
        if not response.ok:
            error_message = json_response.get('message', response.text)
            raise CoinDCXAPIException(
                error_message,
                status_code=response.status_code,
                response=json_response,
            )

        return json_response

    def _get(self, endpoint: str, params: Optional[Dict] = None, use_public_url: bool = False) -> Any:
        """Make GET request (for public endpoints)"""
        return self._request('GET', endpoint, authenticated=False, params=params, use_public_url=use_public_url)

    def _post(self, endpoint: str, data: Optional[Dict] = None) -> Any:
        """Make POST request (for authenticated endpoints)"""
        return self._request('POST', endpoint, authenticated=True, data=data)

    # ===== Public Endpoints =====
    # Delegated to MarketEndpoints

    def get_ticker(self) -> list:
        """
        Get ticker for all trading pairs

        Returns:
            List of ticker data for all markets

        Example:
            >>> client = Client()
            >>> tickers = client.get_ticker()
        """
        return self.market.get_ticker()

    def get_markets(self) -> list:
        """
        Get list of all active markets

        Returns:
            List of market symbols

        Example:
            >>> client = Client()
            >>> markets = client.get_markets()
            >>> print(markets)  # ['SNTBTC', 'TRXBTC', ...]
        """
        return self.market.get_markets()

    def get_markets_details(self) -> list:
        """
        Get detailed information about all markets

        Returns:
            List of market details including precision, limits, etc.

        Example:
            >>> client = Client()
            >>> details = client.get_markets_details()
        """
        return self.market.get_markets_details()

    def get_trades(self, pair: str, limit: int = 30) -> list:
        """
        Get recent trades for a market pair

        Args:
            pair: Market pair (e.g., 'KC-BTC_USDT')
            limit: Number of trades to fetch (default: 30, max: 500)

        Returns:
            List of recent trades

        Example:
            >>> client = Client()
            >>> trades = client.get_trades('KC-BTC_USDT', limit=50)
        """
        return self.market.get_trades(pair, limit)

    def get_orderbook(self, pair: str) -> dict:
        """
        Get order book for a market pair

        Args:
            pair: Market pair (e.g., 'KC-BTC_USDT')

        Returns:
            Order book with bids and asks

        Example:
            >>> client = Client()
            >>> orderbook = client.get_orderbook('KC-BTC_USDT')
            >>> print(orderbook['bids'])
        """
        return self.market.get_orderbook(pair)

    def get_candles(
        self,
        pair: str,
        interval: str,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        limit: int = 500,
    ) -> list:
        """
        Get candlestick data for a market pair

        Args:
            pair: Market pair (e.g., 'KC-BTC_USDT')
            interval: Candlestick interval (e.g., '1m', '5m', '1h', '1d')
            start_time: Start timestamp in milliseconds (optional)
            end_time: End timestamp in milliseconds (optional)
            limit: Number of candles (default: 500, max: 1000)

        Returns:
            List of candlestick data

        Example:
            >>> client = Client()
            >>> candles = client.get_candles('KC-BTC_USDT', '1h', limit=100)
        """
        return self.market.get_candles(pair, interval, start_time, end_time, limit)

    # ===== Authenticated Endpoints =====
    # Delegated to SpotEndpoints

    def get_balances(self) -> list:
        """
        Get account balances for all currencies

        Returns:
            List of balances for each currency

        Example:
            >>> client = Client(api_key='...', api_secret='...')
            >>> balances = client.get_balances()
            >>> for balance in balances:
            ...     print(f"{balance['currency']}: {balance['balance']}")

        Raises:
            CoinDCXAuthenticationException: If API credentials not provided
        """
        return self.spot.get_balances()

    def get_user_info(self) -> dict:
        """
        Get user account information

        Returns:
            User information including ID, name, email, etc.

        Example:
            >>> client = Client(api_key='...', api_secret='...')
            >>> info = client.get_user_info()
            >>> print(info['email'])

        Raises:
            CoinDCXAuthenticationException: If API credentials not provided
        """
        return self.spot.get_user_info()

    def create_spot_order(
        self,
        market: str,
        side: Union[str, OrderSide],
        order_type: Union[str, OrderType],
        total_quantity: float,
        price_per_unit: Optional[float] = None,
        client_order_id: Optional[str] = None,
    ) -> dict:
        """
        Create a spot order

        Args:
            market: Market pair (e.g., 'KC-BTC_USDT', 'KC-ETH_USDT')
            side: Order side - 'buy' or 'sell' (or use OrderSide enum)
            order_type: Order type - 'market_order' or 'limit_order' (or use OrderType enum)
            total_quantity: Total quantity of base currency to buy/sell
            price_per_unit: Price per unit (required for limit orders)
            client_order_id: Optional client order ID for tracking

        Returns:
            Dictionary containing order details

        Raises:
            CoinDCXInvalidOrderException: If required parameters are missing or invalid
            CoinDCXAuthenticationException: If API credentials not provided

        Example:
            >>> client = Client(api_key='...', api_secret='...')
            >>> # Create a limit buy order
            >>> order = client.create_spot_order(
            ...     market='KC-BTC_USDT',
            ...     side=OrderSide.BUY,
            ...     order_type=OrderType.LIMIT_ORDER,
            ...     total_quantity=0.001,
            ...     price_per_unit=50000
            ... )
            >>> print(f"Order ID: {order['id']}, Status: {order['status']}")
        """
        return self.spot.create_order(
            market=market,
            side=side,
            order_type=order_type,
            total_quantity=total_quantity,
            price_per_unit=price_per_unit,
            client_order_id=client_order_id,
        )

    # ===== Futures Endpoints =====
    # Delegated to FuturesEndpoints

    def get_futures_candles(
        self,
        pair: str,
        from_time: int,
        to_time: int,
        resolution: str,
    ) -> dict:
        """
        Get candlestick data for a futures instrument

        Args:
            pair: Futures pair (e.g., 'B-BTC_USDT')
            from_time: Start timestamp in seconds (EPOCH)
            to_time: End timestamp in seconds (EPOCH)
            resolution: Candle resolution - '1' (1min), '5' (5min), '60' (1hour), '1D' (1day)
                       Use FuturesResolution enum for type safety

        Returns:
            Dictionary with candlestick data containing:
                - s: status ("ok" if successful)
                - data: List of candle objects with open, high, low, close, volume, time

        Example:
            >>> from coindcx import Client, FuturesResolution
            >>> import time
            >>> client = Client()
            >>> to_time = int(time.time())
            >>> from_time = to_time - (7 * 24 * 60 * 60)  # 7 days ago
            >>> candles = client.get_futures_candles(
            ...     'B-BTC_USDT',
            ...     from_time,
            ...     to_time,
            ...     FuturesResolution.ONE_DAY
            ... )
            >>> print(f"Received {len(candles['data'])} candles")

        Note:
            - Timestamps should be in seconds, not milliseconds (different from spot candles)
            - Resolution uses different format than spot: '1', '5', '60', '1D'
            - This is a public endpoint, no authentication required
        """
        return self.futures.get_futures_candles(pair, from_time, to_time, resolution)

    def get_active_instruments(self, margin_currency_short_name: Optional[list] = None) -> list:
        """
        Get list of all active futures instruments

        Args:
            margin_currency_short_name: List of margin currencies to filter by (e.g., ['USDT'], ['INR'], or ['USDT', 'INR'])
                                       If not provided, returns instruments for USDT margin mode by default

        Returns:
            List of active instrument pairs (e.g., ['B-BTC_USDT', 'B-ETH_USDT', ...])

        Example:
            >>> client = Client()
            >>> # Get USDT margined instruments
            >>> usdt_instruments = client.get_active_instruments(['USDT'])
            >>> print(f"Total USDT instruments: {len(usdt_instruments)}")
            >>>
            >>> # Get INR margined instruments
            >>> inr_instruments = client.get_active_instruments(['INR'])
            >>>
            >>> # Get both USDT and INR margined instruments
            >>> all_instruments = client.get_active_instruments(['USDT', 'INR'])

        Note:
            - This is a public endpoint, no authentication required
            - Defaults to USDT margin mode if not specified
        """
        return self.futures.get_active_instruments(margin_currency_short_name)

    def get_instrument_details(self, pair: str, margin_currency_short_name: str = 'USDT') -> dict:
        """
        Get detailed information for a specific futures instrument

        Args:
            pair: Futures instrument pair (e.g., 'B-BTC_USDT', 'B-ETH_USDT')
            margin_currency_short_name: Margin currency mode - 'USDT' or 'INR' (default: 'USDT')

        Returns:
            Dictionary containing detailed instrument information including trading rules,
            fees, leverage limits, and other configuration

        Example:
            >>> client = Client()
            >>> # Get BTC futures instrument details
            >>> details = client.get_instrument_details('B-BTC_USDT', 'USDT')
            >>> instrument = details['instrument']
            >>> print(f"Status: {instrument['status']}")
            >>> print(f"Max leverage: {instrument['max_leverage_long']}x")
            >>> print(f"Maker fee: {instrument['maker_fee']}%")

        Note:
            - This is a public endpoint, no authentication required
            - Returns comprehensive instrument configuration and trading rules
        """
        return self.futures.get_instrument_details(pair, margin_currency_short_name)

    def create_futures_order(
        self,
        pair: str,
        side: Union[str, OrderSide],
        order_type: Union[str, FuturesOrderType],
        total_quantity: float,
        notification: Union[str, NotificationType] = NotificationType.NO_NOTIFICATION,
        leverage: Optional[int] = None,
        price: Optional[float] = None,
        stop_price: Optional[float] = None,
        time_in_force: Optional[Union[str, TimeInForce]] = None,
        hidden: bool = False,
        post_only: bool = False,
        margin_currency_short_name: Union[str, FuturesMarginMode] = FuturesMarginMode.USDT,
        position_margin_type: Optional[Union[str, PositionMarginType]] = None,
        take_profit_price: Optional[float] = None,
        stop_loss_price: Optional[float] = None,
    ) -> dict:
        """
        Create a futures order

        Args:
            pair: Futures pair (e.g., 'B-BTC_USDT', 'B-ETH_USDT')
            side: Order side - 'buy' or 'sell' (or use OrderSide enum)
            order_type: Order type - 'market', 'limit', 'stop_limit', 'stop_market',
                       'take_profit_limit', 'take_profit_market' (or use FuturesOrderType enum)
            total_quantity: Total quantity of contracts to trade
            notification: Notification type (default: NO_NOTIFICATION)
            leverage: Leverage multiplier (e.g., 10 for 10x leverage)
            price: Limit price (required for limit-type orders)
            stop_price: Stop/trigger price (required for stop/take-profit orders)
            time_in_force: Time in force - 'good_till_cancel', 'fill_or_kill', 'immediate_or_cancel'
                          Do not include for market orders
            hidden: Whether to hide the order from the orderbook
            post_only: Whether this is a post-only order (maker-only)
            margin_currency_short_name: Margin currency - 'USDT' or 'INR' (default: USDT)
            position_margin_type: Position margin type - 'isolated' or 'crossed'
            take_profit_price: Take profit trigger price (applied to entire position)
            stop_loss_price: Stop loss trigger price (applied to entire position)

        Returns:
            Dictionary containing order details

        Raises:
            CoinDCXInvalidOrderException: If required parameters are missing or invalid
            CoinDCXAuthenticationException: If API credentials not provided

        Example:
            >>> client = Client(api_key='...', api_secret='...')
            >>> # Create a limit buy order with 10x leverage
            >>> order = client.create_futures_order(
            ...     pair='B-BTC_USDT',
            ...     side=OrderSide.BUY,
            ...     order_type=FuturesOrderType.LIMIT,
            ...     total_quantity=0.01,
            ...     price=50000,
            ...     leverage=10
            ... )
            >>> print(f"Order ID: {order['id']}, Status: {order['status']}")
            >>>
            >>> # Create a market sell order with TP/SL
            >>> order = client.create_futures_order(
            ...     pair='B-BTC_USDT',
            ...     side='sell',
            ...     order_type='market',
            ...     total_quantity=0.01,
            ...     leverage=5,
            ...     take_profit_price=55000,
            ...     stop_loss_price=48000
            ... )
        """
        return self.futures.create_order(
            pair=pair,
            side=side,
            order_type=order_type,
            total_quantity=total_quantity,
            notification=notification,
            leverage=leverage,
            price=price,
            stop_price=stop_price,
            time_in_force=time_in_force,
            hidden=hidden,
            post_only=post_only,
            margin_currency_short_name=margin_currency_short_name,
            position_margin_type=position_margin_type,
            take_profit_price=take_profit_price,
            stop_loss_price=stop_loss_price,
        )

    def close(self):
        """Close the client session"""
        self.session.close()

    def __enter__(self):
        """Context manager entry"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.close()
