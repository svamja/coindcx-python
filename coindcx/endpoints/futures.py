"""
CoinDCX Futures Trading Endpoints

Endpoints for futures trading operations.
"""

from typing import Callable, Optional


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
            pair: Futures pair (e.g., 'KC-BTC_USDT')
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
            >>> candles = client.get_futures_candles('KC-BTC_USDT', from_time, to_time, '1D')
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
            List of active instrument pairs (e.g., ['KC-BTC_USDT', 'KC-ETH_USDT', ...])

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
            pair: Futures instrument pair (e.g., 'KC-BTC_USDT', 'KC-ETH_USDT')
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
            >>> btc_details = client.get_instrument_details('KC-BTC_USDT', 'USDT')
            >>> print(f"Status: {btc_details['instrument']['status']}")
            >>> print(f"Max leverage: {btc_details['instrument']['max_leverage_long']}x")
            >>> print(f"Maker fee: {btc_details['instrument']['maker_fee']}%")
            >>> print(f"Min quantity: {btc_details['instrument']['min_quantity']}")
            >>>
            >>> # Get INR margined instrument
            >>> eth_inr = client.get_instrument_details('KC-ETH_USDT', 'INR')

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

    # TODO: Implement authenticated futures trading endpoints
    # - create_futures_order()
    # - cancel_futures_order()
    # - get_futures_positions()
    # - update_leverage()
    # - get_futures_transactions()
    # - get_futures_order_history()
