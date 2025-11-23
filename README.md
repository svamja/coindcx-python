# CoinDCX Python API

A Python wrapper for the CoinDCX API with support for public market data, authenticated trading, and WebSocket streams.

Please note this is NOT officially created or maintained by CoinDCX.

## Features

- ✅ **Single unified client** for both public and authenticated endpoints
- ✅ **Type hints** for better IDE support
- ✅ **Automatic HMAC-SHA256 signature generation**
- ✅ **Comprehensive error handling** with custom exceptions
- ✅ **Support for all CoinDCX endpoints**:
  - Public market data
  - Spot trading
  - Margin trading
  - Futures trading
  - WebSocket streams (coming soon)
- ✅ **Context manager support** for automatic resource cleanup
- ✅ **Enums for constants** (order types, sides, status, etc.)

## Installation

```bash
pip install -e .
```

Or install from requirements:

```bash
pip install -r requirements.txt
```

## Quick Start

### Public Endpoints (No Authentication)

```python
from coindcx import Client

# Initialize client without credentials for public endpoints
client = Client()

# Get all markets
markets = client.get_markets()
print(f"Available markets: {len(markets)}")

# Get ticker for all markets
tickers = client.get_ticker()
for ticker in tickers[:5]:  # Show first 5
    print(f"{ticker['market']}: {ticker['last_price']}")

# Get market details
details = client.get_markets_details()
for market in details[:3]:
    print(f"{market['coindcx_name']}: Min quantity = {market['min_quantity']}")

# Get order book
orderbook = client.get_orderbook('B-BTC_USDT')
print(f"Best bid: {list(orderbook['bids'].keys())[0]}")
print(f"Best ask: {list(orderbook['asks'].keys())[0]}")

# Get recent trades
trades = client.get_trades('B-BTC_USDT', limit=10)
print(f"Latest trade price: {trades[0]['p']}")

# Get candlestick data
candles = client.get_candles('B-BTC_USDT', interval='1h', limit=24)
print(f"24h candles received: {len(candles)}")
```

### Authenticated Endpoints

```python
from coindcx import Client

# Initialize client with API credentials
client = Client(
    api_key='your_api_key_here',
    api_secret='your_api_secret_here'
)

# Get account balances
balances = client.get_balances()
for balance in balances:
    if float(balance['balance']) > 0:
        print(f"{balance['currency']}: {balance['balance']}")

# Get user info
user_info = client.get_user_info()
print(f"User ID: {user_info['coindcx_id']}")
print(f"Email: {user_info['email']}")
```

### Using Context Manager

```python
from coindcx import Client

# Automatically closes session when done
with Client(api_key='...', api_secret='...') as client:
    balances = client.get_balances()
    print(balances)
# Session automatically closed here
```

## Error Handling

The library provides specific exceptions for different error scenarios:

```python
from coindcx import Client, CoinDCXAPIException, CoinDCXAuthenticationException

client = Client()

try:
    # This will fail - authentication required
    balances = client.get_balances()
except CoinDCXAuthenticationException as e:
    print(f"Authentication error: {e}")

try:
    # Invalid market
    orderbook = client.get_orderbook('INVALID_MARKET')
except CoinDCXAPIException as e:
    print(f"API error [{e.status_code}]: {e.message}")
```

### Exception Hierarchy

```
CoinDCXException (base)
├── CoinDCXAPIException          # API errors (4xx, 5xx responses)
├── CoinDCXRequestException      # Network/timeout errors
├── CoinDCXAuthenticationException  # Missing or invalid credentials
├── CoinDCXRateLimitException    # Rate limit exceeded (429)
└── CoinDCXOrderException        # Order-related errors
    └── CoinDCXInvalidOrderException
```

## Using Enums

The library provides enums for various constants:

```python
from coindcx import Client, OrderSide, OrderType, CandleInterval

# Use enums for type safety
candles = client.get_candles(
    pair='B-BTC_USDT',
    interval=CandleInterval.ONE_HOUR,
    limit=100
)
```

Available enums:
- `OrderSide`: BUY, SELL
- `OrderType`: MARKET_ORDER, LIMIT_ORDER, STOP_LIMIT, TAKE_PROFIT
- `OrderStatus`: INIT, OPEN, FILLED, CANCELLED, etc.
- `CandleInterval`: ONE_MINUTE, FIVE_MINUTES, ONE_HOUR, ONE_DAY, etc.
- `ExchangeCode`: COINDCX_INR, BINANCE, HUOBI, KUCOIN
- `TimeInForce`: GOOD_TILL_CANCEL, IMMEDIATE_OR_CANCEL, FILL_OR_KILL
- `FuturesMarginMode`: INR, USDT
- `PositionMarginType`: ISOLATED, CROSSED

## API Coverage

### ✅ Implemented

**Public Endpoints:**
- `get_ticker()` - Get ticker for all markets
- `get_markets()` - Get list of all markets
- `get_markets_details()` - Get detailed market information
- `get_trades(pair, limit)` - Get recent trades
- `get_orderbook(pair)` - Get order book
- `get_candles(pair, interval, ...)` - Get candlestick data

**Authenticated Endpoints:**
- `get_balances()` - Get account balances
- `get_user_info()` - Get user information

### 🚧 Coming Soon

**Spot Trading:**
- Create order
- Cancel order
- Get order status
- Get active orders
- Get trade history

**Margin Trading:**
- Place margin order
- Cancel margin order
- Edit target/stop-loss
- Add/remove margin

**Futures Trading:**
- Create futures order
- List positions
- Update leverage
- Get transactions

**WebSocket Streams:**
- Balance updates
- Order updates
- Trade updates
- Price feeds
- Order book streams

## Configuration

You can customize the client behavior:

```python
from coindcx import Client

client = Client(
    api_key='your_key',
    api_secret='your_secret',
    timeout=60,  # Request timeout in seconds (default: 30)
    base_url='https://api.coindcx.com',  # Override base URL if needed
    public_url='https://public.coindcx.com',  # Override public URL
)
```

## Development

### Project Structure

```
coindcx_api/
├── coindcx/
│   ├── __init__.py
│   ├── client.py          # Main Client class
│   ├── exceptions.py      # Custom exceptions
│   ├── enums.py          # Enums and constants
│   └── endpoints/        # Future: Modular endpoint implementations
│       ├── __init__.py
│       ├── market.py     # Public market endpoints
│       ├── spot.py       # Spot trading
│       ├── margin.py     # Margin trading
│       └── futures.py    # Futures trading
├── examples/
│   └── basic_usage.py
├── setup.py
├── requirements.txt
└── README.md
```

### Running Examples

```bash
# Set your API credentials as environment variables (optional)
export COINDCX_API_KEY="your_api_key"
export COINDCX_API_SECRET="your_api_secret"

# Run examples
python examples/basic_usage.py
```

## Getting API Credentials

1. Sign up at [CoinDCX](https://coindcx.com)
2. Go to [API Dashboard](https://coindcx.com/api-dashboard)
3. Click "Create API Key"
4. Store your key and secret securely

**Security Notes:**
- Never commit API credentials to version control
- Use environment variables for credentials in production
- Bind API keys to specific IP addresses when possible
- Regularly rotate your API keys

## Rate Limits

CoinDCX enforces rate limits on API calls. The library will raise `CoinDCXRateLimitException` when limits are exceeded.

| Endpoint | Limit | Period |
|----------|-------|--------|
| Create Order | 2000 | 60s |
| Cancel Order | 2000 | 60s |
| Order Status | 2000 | 60s |
| Active Orders | 300 | 60s |

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

## Disclaimer

This library is not officially affiliated with CoinDCX. Use at your own risk. Trading cryptocurrencies carries risk - ensure you understand the risks before trading.

## Support

- [CoinDCX API Documentation](https://docs.coindcx.com)
- [CoinDCX Support](https://support.coindcx.com)

## Changelog

### v0.1.0 (2024-01-XX)
- Initial release
- Support for public market data endpoints
- Support for basic authenticated endpoints
- HMAC-SHA256 signature generation
- Comprehensive error handling

---

# Development Notes

## How to prepare markdown documentation

1. Use https://github.com/Goldziher/html-to-markdown
   Online https://goldziher.github.io/html-to-markdown/
2. Copy HTML from https://docs.coindcx.com/
3. Copy the output markdown to "coindcx_documentation.md"
