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

    # TODO: Implement authenticated futures trading endpoints
    # - create_futures_order()
    # - cancel_futures_order()
    # - get_futures_positions()
    # - update_leverage()
    # - get_futures_transactions()
    # - get_futures_order_history()
