"""
CoinDCX Market Data Endpoints

Public endpoints for market data including ticker, trades, orderbook, and candles.
"""

from typing import Optional, Any, Dict, Callable


class MarketEndpoints:
    """
    Market data endpoints (public, no authentication required)

    Handles all public market data endpoints including:
    - Ticker data
    - Market lists
    - Trade history
    - Order books
    - Candlestick data
    """

    def __init__(self, request_handler: Callable):
        """
        Initialize market endpoints

        Args:
            request_handler: Function to make HTTP requests (typically client._get)
        """
        self._get = request_handler

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
            pair: Market pair (e.g., 'KC-BTC_USDT')
            limit: Number of trades to fetch (default: 30, max: 500)

        Returns:
            List of recent trades

        Example:
            >>> client = Client()
            >>> trades = client.get_trades('KC-BTC_USDT', limit=50)
        """
        params = {'pair': pair, 'limit': limit}
        return self._get('/market_data/trade_history', params=params, use_public_url=True)

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
