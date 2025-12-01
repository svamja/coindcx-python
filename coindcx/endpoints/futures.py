"""
CoinDCX Futures Trading Endpoints

Endpoints for futures trading operations.
"""

from typing import Callable, Optional, Union
from ..enums import (
    OrderSide,
    FuturesOrderType,
    NotificationType,
    TimeInForce,
    FuturesMarginMode,
    PositionMarginType,
)
from ..exceptions import CoinDCXInvalidOrderException


class FuturesEndpoints:
    """
    Futures trading endpoints

    Handles both public and authenticated endpoints for futures trading including:
    - Get futures candles (public)
    - Get active instruments (public)
    - Get instrument details (public)
    - Create futures order (authenticated)
    - Cancel futures order (authenticated)
    - Get futures positions (authenticated)
    - Update leverage (authenticated)
    - Get futures transactions (authenticated)
    - Get futures order history (authenticated)
    """

    def __init__(self, get_handler: Callable, post_handler: Callable):
        """
        Initialize futures trading endpoints

        Args:
            get_handler: Function to make public HTTP GET requests (typically client._get)
            post_handler: Function to make authenticated HTTP POST requests (typically client._post)
        """
        self._get = get_handler
        self._post = post_handler

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

        Returns:
            Dictionary with candlestick data containing:
                - s: status ("ok" if successful)
                - data: List of candle objects with open, high, low, close, volume, time

        Example:
            >>> client = Client()
            >>> # Get 1-day candles for BTC futures
            >>> import time
            >>> to_time = int(time.time())
            >>> from_time = to_time - (7 * 24 * 60 * 60)  # 7 days ago
            >>> candles = client.get_futures_candles('B-BTC_USDT', from_time, to_time, '1D')
            >>> print(f"Status: {candles['s']}")
            >>> for candle in candles['data']:
            ...     print(f"Open: {candle['open']}, Close: {candle['close']}")

        Note:
            - Timestamps should be in seconds, not milliseconds (different from spot candles)
            - Resolution uses different format than spot: '1', '5', '60', '1D' instead of '1m', '5m', '1h', '1d'
            - This is a public endpoint, no authentication required
        """
        params = {
            'pair': pair,
            'from': from_time,
            'to': to_time,
            'resolution': resolution,
            'pcode': 'f',  # Static value 'f' denotes futures product
        }

        return self._get('/market_data/candlesticks', params=params, use_public_url=True)

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
            >>> print(f"USDT instruments: {len(usdt_instruments)}")
            >>> print(usdt_instruments[:5])
            >>>
            >>> # Get INR margined instruments
            >>> inr_instruments = client.get_active_instruments(['INR'])
            >>> print(f"INR instruments: {len(inr_instruments)}")
            >>>
            >>> # Get both USDT and INR margined instruments
            >>> all_instruments = client.get_active_instruments(['USDT', 'INR'])

        Note:
            - This is a public endpoint, no authentication required
            - Defaults to USDT margin mode if not specified
        """
        if margin_currency_short_name is None:
            margin_currency_short_name = ['USDT']

        # Build query parameters with array notation
        params = {}
        for currency in margin_currency_short_name:
            params[f'margin_currency_short_name[]'] = currency

        return self._get('/exchange/v1/derivatives/futures/data/active_instruments', params=params)

    def get_instrument_details(self, pair: str, margin_currency_short_name: str = 'USDT') -> dict:
        """
        Get detailed information for a specific futures instrument

        Args:
            pair: Futures instrument pair (e.g., 'B-BTC_USDT', 'B-ETH_USDT')
            margin_currency_short_name: Margin currency mode - 'USDT' or 'INR' (default: 'USDT')

        Returns:
            Dictionary containing detailed instrument information including:
                - settle_currency_short_name: Currency for settlement
                - quote_currency_short_name: Quote currency
                - position_currency_short_name: Position currency
                - status: 'active' or 'inactive'
                - kind: Contract type (e.g., 'perpetual')
                - max_leverage_long: Maximum leverage for long positions
                - max_leverage_short: Maximum leverage for short positions
                - price_increment: Minimum price step
                - quantity_increment: Minimum quantity step
                - min_quantity: Minimum order quantity
                - max_quantity: Maximum order quantity
                - min_notional: Minimum order value
                - maker_fee: Maker fee percentage
                - taker_fee: Taker fee percentage
                - funding_frequency: Funding interval in hours
                - order_types: List of supported order types
                - time_in_force_options: List of supported time-in-force options
                - dynamic_position_leverage_details: Leverage limits by position size
                - And many more fields...

        Example:
            >>> client = Client()
            >>> # Get BTC futures instrument details (USDT margin)
            >>> btc_details = client.get_instrument_details('B-BTC_USDT', 'USDT')
            >>> print(f"Status: {btc_details['instrument']['status']}")
            >>> print(f"Max leverage: {btc_details['instrument']['max_leverage_long']}x")
            >>> print(f"Maker fee: {btc_details['instrument']['maker_fee']}%")
            >>> print(f"Min quantity: {btc_details['instrument']['min_quantity']}")
            >>>
            >>> # Get INR margined instrument
            >>> eth_inr = client.get_instrument_details('B-ETH_USDT', 'INR')

        Note:
            - This is a public endpoint, no authentication required
            - Returns comprehensive instrument configuration and trading rules
            - Useful for validating order parameters before placing orders
        """
        params = {
            'pair': pair,
            'margin_currency_short_name': margin_currency_short_name
        }

        return self._get('/exchange/v1/derivatives/futures/data/instrument', params=params)

    def create_order(
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
            Dictionary containing order details including:
                - id: Order ID
                - status: Order status
                - side: Order side
                - order_type: Order type
                - pair: Futures pair
                - total_quantity: Total quantity
                - remaining_quantity: Remaining quantity
                - price: Order price
                - leverage: Leverage used
                - created_at: Order creation timestamp

        Raises:
            CoinDCXInvalidOrderException: If required parameters are missing or invalid
            CoinDCXAuthenticationException: If API credentials not provided
            CoinDCXAPIException: For API errors

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
            >>> # Create a market sell order with TP/SL triggers
            >>> order = client.create_futures_order(
            ...     pair='B-BTC_USDT',
            ...     side='sell',
            ...     order_type='market',
            ...     total_quantity=0.01,
            ...     leverage=5,
            ...     take_profit_price=55000,
            ...     stop_loss_price=48000
            ... )
            >>>
            >>> # Create a stop-limit order
            >>> order = client.create_futures_order(
            ...     pair='B-BTC_USDT',
            ...     side='buy',
            ...     order_type=FuturesOrderType.STOP_LIMIT,
            ...     total_quantity=0.01,
            ...     price=49000,
            ...     stop_price=49500,
            ...     leverage=10,
            ...     time_in_force=TimeInForce.GOOD_TILL_CANCEL
            ... )

        Note:
            - Rate limit: 2000 requests per 60 seconds
            - Do not include time_in_force for market orders
            - TP/SL validation rules:
              * Buy Orders: stop_loss_price < LTP < take_profit_price
              * Sell Orders: take_profit_price < LTP < stop_loss_price
            - Take profit/stop loss triggers apply to your entire position
            - Use B- prefix for futures pairs
        """
        # Validate parameters for limit-type orders
        limit_types = [
            FuturesOrderType.LIMIT,
            FuturesOrderType.STOP_LIMIT,
            FuturesOrderType.TAKE_PROFIT_LIMIT,
            "limit",
            "stop_limit",
            "take_profit_limit"
        ]
        if order_type in limit_types and price is None:
            raise CoinDCXInvalidOrderException(
                "price is required for limit-type orders"
            )

        # Validate parameters for stop/take-profit orders
        stop_types = [
            FuturesOrderType.STOP_LIMIT,
            FuturesOrderType.STOP_MARKET,
            FuturesOrderType.TAKE_PROFIT_LIMIT,
            FuturesOrderType.TAKE_PROFIT_MARKET,
            "stop_limit",
            "stop_market",
            "take_profit_limit",
            "take_profit_market"
        ]
        if order_type in stop_types and stop_price is None:
            raise CoinDCXInvalidOrderException(
                "stop_price is required for stop/take-profit orders"
            )

        # Build nested request structure
        order_data = {
            "side": side.value if isinstance(side, OrderSide) else side,
            "pair": pair,
            "order_type": order_type.value if isinstance(order_type, FuturesOrderType) else order_type,
            "total_quantity": total_quantity,
        }

        # Add optional parameters
        if leverage is not None:
            order_data["leverage"] = leverage
        if price is not None:
            order_data["price"] = price
        if stop_price is not None:
            order_data["stop_price"] = stop_price
        if time_in_force is not None:
            order_data["time_in_force"] = (
                time_in_force.value if isinstance(time_in_force, TimeInForce) else time_in_force
            )
        if position_margin_type is not None:
            order_data["position_margin_type"] = (
                position_margin_type.value if isinstance(position_margin_type, PositionMarginType)
                else position_margin_type
            )
        if take_profit_price is not None:
            order_data["take_profit_price"] = take_profit_price
        if stop_loss_price is not None:
            order_data["stop_loss_price"] = stop_loss_price

        # Build final request with nested structure
        margin_currency_short_name = margin_currency_short_name.value if isinstance(margin_currency_short_name, FuturesMarginMode) else margin_currency_short_name
        order_data["margin_currency_short_name"] = margin_currency_short_name
        data = {
            "order": order_data,
        }

        # Make request (timestamp added automatically by _post)
        response = self._post('/exchange/v1/derivatives/futures/orders/create', data=data)

        # Extract first order from array response
        if isinstance(response, list) and len(response) > 0:
            return response[0]

        return response

    def list_orders(
        self,
        side: Union[str, OrderSide],
        status: str = "open",
        page: int = 1,
        size: int = 10,
        margin_currency_short_name: Optional[list] = None,
    ) -> list:
        """
        List futures orders based on status and side

        Args:
            side: Order side - 'buy' or 'sell' (or use OrderSide enum)
            status: Comma separated statuses (e.g., 'open', 'filled', 'cancelled')
                   Default: 'open'
            page: Page number (default: 1)
            size: Number of records per page (default: 10)
            margin_currency_short_name: List of margin currencies (e.g., ['USDT'])
                                       Default: ['USDT']

        Returns:
            List of orders matching the criteria

        Example:
            >>> client = Client()
            >>> # List open buy orders
            >>> orders = client.list_orders(side='buy', status='open')
            >>>
            >>> # List filled sell orders
            >>> history = client.list_orders(
            ...     side=OrderSide.SELL,
            ...     status='filled',
            ...     page=1,
            ...     size=20
            ... )
        """
        if margin_currency_short_name is None:
            margin_currency_short_name = ['USDT']

        data = {
            "side": side.value if isinstance(side, OrderSide) else side,
            "status": status,
            "page": str(page),
            "size": str(size),
            "margin_currency_short_name": margin_currency_short_name
        }

        return self._post('/exchange/v1/derivatives/futures/orders', data=data)

    def edit_order(
        self,
        id: str,
        total_quantity: float,
        price: float,
        take_profit_price: Optional[float] = None,
        stop_loss_price: Optional[float] = None,
    ) -> list:
        """
        Edit an open futures order

        Args:
            id: Order ID
            total_quantity: New total quantity
            price: New price
            take_profit_price: New take profit trigger price (optional)
            stop_loss_price: New stop loss trigger price (optional)

        Returns:
            List containing the edited order details

        Note:
            - Edit order is only supported on USDT margined Futures at the moment.
            - Only open orders can be edited.
            - This endpoint accepts limit price and quantity updates
        """
        data = {
            "id": id,
            "total_quantity": total_quantity,
            "price": price,
        }

        if take_profit_price is not None:
            data["take_profit_price"] = take_profit_price
        if stop_loss_price is not None:
            data["stop_loss_price"] = stop_loss_price

        return self._post('/exchange/v1/derivatives/futures/orders/edit', data=data)

    def get_trade_history(self, pair: str) -> list:
        """
        Get real-time trade history for a futures instrument

        Args:
            pair: Futures pair (e.g., 'B-BTC_USDT')

        Returns:
            List of trade dictionaries containing:
                - price: Trade price
                - quantity: Trade quantity
                - timestamp: Trade timestamp
                - is_maker: Boolean indicating if trade was maker

        Example:
            >>> client = Client()
            >>> trades = client.get_futures_trade_history('B-BTC_USDT')
            >>> for trade in trades[:5]:
            ...     print(f"Price: {trade['price']}, Quantity: {trade['quantity']}")

        Note:
            - This is a public endpoint, no authentication required
            - Authentication wrapper handles endpoint access correctly
        """
        return self._get(
            '/exchange/v1/derivatives/futures/data/trades',
            params={'pair': pair},
            use_public_url=False
        )

    # TODO: Implement remaining authenticated futures trading endpoints
    # - cancel_futures_order()
    # - get_futures_positions()
    # - update_leverage()
    # - get_futures_transactions()
    # - get_futures_order_history()
