"""
CoinDCX API Client

A unified client for accessing both public and authenticated CoinDCX API endpoints.
"""

import hmac
import hashlib
import json
import time
from typing import Dict, Optional, Any
from urllib.parse import urljoin

import requests

from .exceptions import (
    CoinDCXAPIException,
    CoinDCXRequestException,
    CoinDCXAuthenticationException,
    CoinDCXRateLimitException,
)
from .enums import API_BASE_URL, PUBLIC_BASE_URL


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

    def get_ticker(self) -> list:
        """
        Get ticker for all trading pairs

        Returns:
            List of ticker data for all markets

        Example:
            >>> client = Client()
            >>> tickers = client.get_ticker()
        """
        return self._get('/exchange/ticker')

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
        return self._get('/exchange/v1/markets')

    def get_markets_details(self) -> list:
        """
        Get detailed information about all markets

        Returns:
            List of market details including precision, limits, etc.

        Example:
            >>> client = Client()
            >>> details = client.get_markets_details()
        """
        return self._get('/exchange/v1/markets_details')

    def get_trades(self, pair: str, limit: int = 30) -> list:
        """
        Get recent trades for a market pair

        Args:
            pair: Market pair (e.g., 'B-BTC_USDT')
            limit: Number of trades to fetch (default: 30, max: 500)

        Returns:
            List of recent trades

        Example:
            >>> client = Client()
            >>> trades = client.get_trades('B-BTC_USDT', limit=50)
        """
        params = {'pair': pair, 'limit': limit}
        return self._get('/market_data/trade_history', params=params, use_public_url=True)

    def get_orderbook(self, pair: str) -> dict:
        """
        Get order book for a market pair

        Args:
            pair: Market pair (e.g., 'B-BTC_USDT')

        Returns:
            Order book with bids and asks

        Example:
            >>> client = Client()
            >>> orderbook = client.get_orderbook('B-BTC_USDT')
            >>> print(orderbook['bids'])
        """
        params = {'pair': pair}
        return self._get('/market_data/orderbook', params=params, use_public_url=True)

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
            pair: Market pair (e.g., 'B-BTC_USDT')
            interval: Candlestick interval (e.g., '1m', '5m', '1h', '1d')
            start_time: Start timestamp in milliseconds (optional)
            end_time: End timestamp in milliseconds (optional)
            limit: Number of candles (default: 500, max: 1000)

        Returns:
            List of candlestick data

        Example:
            >>> client = Client()
            >>> candles = client.get_candles('B-BTC_USDT', '1h', limit=100)
        """
        params = {
            'pair': pair,
            'interval': interval,
            'limit': limit,
        }

        if start_time:
            params['startTime'] = start_time
        if end_time:
            params['endTime'] = end_time

        return self._get('/market_data/candles', params=params, use_public_url=True)

    # ===== Authenticated Endpoints =====

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
        return self._post('/exchange/v1/users/balances')

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
        return self._post('/exchange/v1/users/info')

    def close(self):
        """Close the client session"""
        self.session.close()

    def __enter__(self):
        """Context manager entry"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.close()
