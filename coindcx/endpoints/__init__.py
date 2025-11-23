"""
CoinDCX API Endpoints

This package contains modular endpoint implementations organized by functionality:
- market: Public market data endpoints
- spot: Spot trading and account endpoints
- margin: Margin trading endpoints
- futures: Futures trading endpoints
"""

from .market import MarketEndpoints
from .spot import SpotEndpoints
from .margin import MarginEndpoints
from .futures import FuturesEndpoints

__all__ = [
    'MarketEndpoints',
    'SpotEndpoints',
    'MarginEndpoints',
    'FuturesEndpoints',
]
