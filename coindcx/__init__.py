"""
CoinDCX Python API Library

A Python wrapper for the CoinDCX API with support for:
- Public market data endpoints
- Authenticated trading endpoints
- Spot trading
- Margin trading
- Futures trading
- WebSocket streams

Example:
    # Public endpoints
    from coindcx import Client

    client = Client()
    markets = client.get_markets()
    ticker = client.get_ticker()

    # Authenticated endpoints
    client = Client(api_key='your_key', api_secret='your_secret')
    balances = client.get_balances()
"""

__version__ = '0.1.0'
__author__ = 'Your Name'

from .client import Client
from .exceptions import (
    CoinDCXException,
    CoinDCXAPIException,
    CoinDCXRequestException,
    CoinDCXAuthenticationException,
    CoinDCXRateLimitException,
    CoinDCXOrderException,
    CoinDCXInvalidOrderException,
)
from .enums import (
    OrderSide,
    OrderType,
    OrderStatus,
    MarginOrderType,
    MarginOrderStatus,
    FuturesOrderType,
    FuturesOrderStatus,
    TimeInForce,
    ExchangeCode,
    CandleInterval,
    FuturesMarginMode,
    PositionMarginType,
    NotificationType,
)

__all__ = [
    # Client
    'Client',
    # Exceptions
    'CoinDCXException',
    'CoinDCXAPIException',
    'CoinDCXRequestException',
    'CoinDCXAuthenticationException',
    'CoinDCXRateLimitException',
    'CoinDCXOrderException',
    'CoinDCXInvalidOrderException',
    # Enums
    'OrderSide',
    'OrderType',
    'OrderStatus',
    'MarginOrderType',
    'MarginOrderStatus',
    'FuturesOrderType',
    'FuturesOrderStatus',
    'TimeInForce',
    'ExchangeCode',
    'CandleInterval',
    'FuturesMarginMode',
    'PositionMarginType',
    'NotificationType',
]
