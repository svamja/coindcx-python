"""
CoinDCX API Enums and Constants
"""

from enum import Enum


class OrderSide(str, Enum):
    """Order side"""
    BUY = "buy"
    SELL = "sell"


class OrderType(str, Enum):
    """Order types for spot trading"""
    MARKET_ORDER = "market_order"
    LIMIT_ORDER = "limit_order"
    STOP_LIMIT = "stop_limit"
    TAKE_PROFIT = "take_profit"


class OrderStatus(str, Enum):
    """Order status"""
    INIT = "init"
    OPEN = "open"
    PARTIALLY_FILLED = "partially_filled"
    FILLED = "filled"
    PARTIALLY_CANCELLED = "partially_cancelled"
    CANCELLED = "cancelled"
    REJECTED = "rejected"


class MarginOrderType(str, Enum):
    """Order types for margin trading"""
    MARKET_ORDER = "market_order"
    LIMIT_ORDER = "limit_order"
    STOP_LIMIT = "stop_limit"
    TAKE_PROFIT = "take_profit"


class MarginOrderStatus(str, Enum):
    """Margin order status"""
    INIT = "init"
    OPEN = "open"
    PARTIAL_ENTRY = "partial_entry"
    PARTIAL_CLOSE = "partial_close"
    CANCELLED = "cancelled"
    REJECTED = "rejected"
    CLOSE = "close"
    TRIGGERED = "triggered"


class FuturesOrderType(str, Enum):
    """Order types for futures trading"""
    MARKET = "market"
    LIMIT = "limit"
    STOP_LIMIT = "stop_limit"
    STOP_MARKET = "stop_market"
    TAKE_PROFIT_LIMIT = "take_profit_limit"
    TAKE_PROFIT_MARKET = "take_profit_market"


class FuturesOrderStatus(str, Enum):
    """Futures order status"""
    OPEN = "open"
    FILLED = "filled"
    PARTIALLY_FILLED = "partially_filled"
    PARTIALLY_CANCELLED = "partially_cancelled"
    CANCELLED = "cancelled"
    REJECTED = "rejected"
    UNTRIGGERED = "untriggered"


class TimeInForce(str, Enum):
    """Time in force options for futures"""
    GOOD_TILL_CANCEL = "good_till_cancel"
    IMMEDIATE_OR_CANCEL = "immediate_or_cancel"
    FILL_OR_KILL = "fill_or_kill"


class ExchangeCode(str, Enum):
    """Exchange codes"""
    COINDCX_INR = "I"
    BINANCE = "B"
    HUOBI = "HB"
    KUCOIN = "KC"


class CandleInterval(str, Enum):
    """Candlestick intervals"""
    ONE_MINUTE = "1m"
    FIVE_MINUTES = "5m"
    FIFTEEN_MINUTES = "15m"
    THIRTY_MINUTES = "30m"
    ONE_HOUR = "1h"
    TWO_HOURS = "2h"
    FOUR_HOURS = "4h"
    SIX_HOURS = "6h"
    EIGHT_HOURS = "8h"
    ONE_DAY = "1d"
    THREE_DAYS = "3d"
    ONE_WEEK = "1w"
    ONE_MONTH = "1M"


class FuturesMarginMode(str, Enum):
    """Futures margin mode"""
    INR = "INR"
    USDT = "USDT"


class PositionMarginType(str, Enum):
    """Position margin type for futures"""
    ISOLATED = "isolated"
    CROSSED = "crossed"


class NotificationType(str, Enum):
    """Notification type for orders"""
    NO_NOTIFICATION = "no_notification"
    EMAIL_NOTIFICATION = "email_notification"
    PUSH_NOTIFICATION = "push_notification"


# API Base URLs
API_BASE_URL = "https://api.coindcx.com"
PUBLIC_BASE_URL = "https://public.coindcx.com"
STREAM_URL = "https://stream.coindcx.com"
