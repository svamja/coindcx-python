# CoinDCX Python API
[![PyPI version](https://img.shields.io/pypi/v/coindcx.svg)](https://pypi.org/project/coindcx/)
[![License](https://img.shields.io/pypi/l/python-binance.svg)](https://pypi.org/project/coindcx/)
[![Supported Versions](https://img.shields.io/pypi/pyversions/coindcx.svg)](https://pypi.org/project/coindcx/)


This is an unofficial Python wrapper for the [CoinDCX Exchange API](https://coindcx.com/api/help/API%20Dashboard/) with support for public market data and authenticated trading.

## Features

- ✅ **Single unified client** for both public and authenticated endpoints
- ✅ **Generic CLI tool** for command-line usage with automatic method discovery
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
pip install coindcx
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
orderbook = client.get_orderbook('KC-BTC_USDT')
print(f"Best bid: {list(orderbook['bids'].keys())[0]}")
print(f"Best ask: {list(orderbook['asks'].keys())[0]}")

# Get recent trades
trades = client.get_trades('KC-BTC_USDT', limit=10)
print(f"Latest trade price: {trades[0]['p']}")

# Get candlestick data
candles = client.get_candles('KC-BTC_USDT', interval='1h', limit=24)
print(f"24h candles received: {len(candles)}")
```

### Futures Endpoints (Public)

```python
from coindcx import Client
import time

client = Client()

# Get all active USDT margined futures instruments
instruments = client.get_active_instruments(['USDT'])
print(f"Total USDT instruments: {len(instruments)}")
print(f"Sample instruments: {instruments[:5]}")

# Get detailed information for a specific instrument
details = client.get_instrument_details('B-BTC_USDT', 'USDT')
instrument = details['instrument']
print(f"Status: {instrument['status']}")
print(f"Max leverage: {instrument['max_leverage_long']}x")
print(f"Maker fee: {instrument['maker_fee']}%")
print(f"Min quantity: {instrument['min_quantity']}")

# Get futures candlestick data
to_time = int(time.time())
from_time = to_time - (7 * 24 * 60 * 60)  # 7 days ago
candles = client.get_futures_candles('B-BTC_USDT', from_time, to_time, '1D')
print(f"Futures candles: {len(candles['data'])}")

# Get futures trade history
trades = client.get_futures_trade_history('B-BTC_USDT')
for trade in trades[:5]:
    print(f"Trade: {trade['quantity']} @ {trade['price']} (Maker: {trade['is_maker']})")
```

### Authenticated Endpoints

```python
from coindcx import Client, OrderSide, OrderType, FuturesOrderType, TimeInForce

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

### Spot Trading

```python
from coindcx import Client, OrderSide, OrderType

client = Client(api_key='your_key', api_secret='your_secret')

# Create a market buy order - buy 0.001 BTC at market price
market_order = client.create_spot_order(
    market='KC-BTC_USDT',
    side=OrderSide.BUY,
    order_type=OrderType.MARKET_ORDER,
    total_quantity=0.001
)
print(f"Market Order ID: {market_order['id']}, Status: {market_order['status']}")

# Create a limit sell order - sell 0.001 BTC at $52,000
limit_order = client.create_spot_order(
    market='KC-BTC_USDT',
    side=OrderSide.SELL,
    order_type=OrderType.LIMIT_ORDER,
    total_quantity=0.001,
    price_per_unit=52000,
    client_order_id='my-custom-order-id'  # Optional tracking ID
)
print(f"Limit Order ID: {limit_order['id']}, Price: {limit_order['price_per_unit']}")
```

### Futures Trading

```python
from coindcx import Client, OrderSide, FuturesOrderType, TimeInForce

client = Client(api_key='your_key', api_secret='your_secret')

# Create a market futures order with 10x leverage
futures_market = client.create_futures_order(
    pair='B-BTC_USDT',
    side=OrderSide.BUY,
    order_type=FuturesOrderType.MARKET,
    total_quantity=0.01,
    leverage=10,
    margin_currency_short_name='USDT'
)
print(f"Futures Market Order: {futures_market['id']}, Leverage: {futures_market['leverage']}x")

# Create a limit futures order with take profit and stop loss
futures_limit = client.create_futures_order(
    pair='B-BTC_USDT',
    side=OrderSide.BUY,
    order_type=FuturesOrderType.LIMIT,
    total_quantity=0.01,
    price=49000,
    leverage=5,
    time_in_force=TimeInForce.GOOD_TILL_CANCEL,
    take_profit_price=55000,  # Take profit at $55,000
    stop_loss_price=47000,    # Stop loss at $47,000
    post_only=True           # Maker-only order
)
print(f"Futures Limit Order: {futures_limit['id']}")

# Create a stop-limit order (triggered when price hits stop_price)
stop_limit = client.create_futures_order(
    pair='B-ETH_USDT',
    side=OrderSide.SELL,
    order_type=FuturesOrderType.STOP_LIMIT,
    total_quantity=0.1,
    price=3200,        # Limit price once triggered
    stop_price=3250,   # Trigger price
    leverage=3,
    time_in_force=TimeInForce.FILL_OR_KILL
)

# Create a take profit market order
take_profit = client.create_futures_order(
    pair='B-BTC_USDT',
    side=OrderSide.SELL,
    order_type=FuturesOrderType.TAKE_PROFIT_MARKET,
    total_quantity=0.005,
    stop_price=60000,  # Trigger when BTC hits $60,000
    leverage=2
)

# List open futures orders
open_orders = client.list_futures_orders(
    side=OrderSide.BUY,
    status='open',
    margin_currency_short_name=['USDT']
)
print(f"Open Orders: {len(open_orders)}")

# Edit an existing futures order
edited_order = client.edit_futures_order(
    id='order_id_here',
    total_quantity=0.5,
    price=51000,
    take_profit_price=55000,
    stop_loss_price=48000
)
print(f"Edited Order ID: {edited_order['id']}")
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

## Command-Line Interface (CLI)

The library includes a powerful generic CLI tool that automatically exposes all client methods for command-line usage. Perfect for quick testing, scripting, and automation.

### Features

- **Automatic method discovery** - Works with all current and future methods without modification
- **Type inference** - Automatically converts arguments to correct types
- **Environment variable support** - Securely pass API credentials
- **Pretty JSON output** - Formatted for readability
- **Built-in help** - View all available methods and their parameters

### Basic Usage

```bash
# View all available methods and their parameters
python cli.py --help

# Call any method with named parameters
python cli.py [method_name] --arg1=value1 --arg2=value2
```

### Examples

**Public Endpoints (No Authentication):**

```bash
# Get all markets
python cli.py get_markets

# Get ticker data for all markets
python cli.py get_ticker

# Get recent trades with parameters
python cli.py get_trades --pair=KC-BTC_USDT --limit=10

# Get order book for a specific pair
python cli.py get_orderbook --pair=KC-BTC_USDT

# Get candlestick data
python cli.py get_candles --pair=KC-BTC_USDT --interval=1h --limit=24

# Get markets details
python cli.py get_markets_details

# Get futures candles
python cli.py get_futures_candles --pair=B-BTC_USDT --from_time=1700000000 --to_time=1700086400 --resolution=1D

# Get futures trade history
python cli.py get_futures_trade_history --pair=B-BTC_USDT

# Get active futures instruments (JSON format or comma-separated)
python cli.py get_active_instruments --margin_currency_short_name=["USDT"]
python cli.py get_active_instruments --margin_currency_short_name=USDT,INR

# Get instrument details
python cli.py get_instrument_details --pair=B-BTC_USDT --margin_currency_short_name=USDT
```

**Authenticated Endpoints:**

```bash
# Option 1: Pass credentials as arguments
python cli.py get_balances --api-key=YOUR_KEY --api-secret=YOUR_SECRET
python cli.py get_user_info --api-key=YOUR_KEY --api-secret=YOUR_SECRET

# Option 2: Use environment variables (recommended for security)
export COINDCX_API_KEY="your_api_key"
export COINDCX_API_SECRET="your_api_secret"
python cli.py get_balances
python cli.py get_user_info

# Create spot orders
python cli.py create_spot_order --market=KC-BTC_USDT --side=buy --order_type=market_order --total_quantity=0.001

python cli.py create_spot_order --market=KC-ETH_USDT --side=sell --order_type=limit_order --total_quantity=0.1 --price_per_unit=3500 --client_order_id=my-custom-id

# Create futures orders
python cli.py create_futures_order --pair=B-BTC_USDT --side=buy --order_type=market --total_quantity=0.01 --leverage=10 --margin_currency_short_name=USDT

python cli.py create_futures_order --pair=B-BTC_USDT --side=buy --order_type=limit --total_quantity=0.01 --price=50000 --leverage=5 --time_in_force=good_till_cancel

# List futures orders
python cli.py list_futures_orders --side=buy --status=open

# Edit futures order
python cli.py edit_futures_order --id=ORDER_ID --total_quantity=0.5 --price=51000
```

**Additional Options:**

```bash
# Customize timeout
python cli.py get_candles --pair=KC-BTC_USDT --interval=1h --timeout=60

# Disable pretty printing (compact JSON)
python cli.py get_markets --pretty=false
```

### How It Works

The CLI uses Python's introspection to:
1. Discover all public methods from the `Client` class
2. Extract type hints and parameter information
3. Automatically convert string arguments to the correct types (int, float, bool, etc.)
4. Validate required vs optional parameters

**This means any new methods you add to the Client class are automatically available in the CLI without any changes!**

### CLI Options

| Option | Description | Example |
|--------|-------------|---------|
| `--api-key` | API key for authentication | `--api-key=YOUR_KEY` |
| `--api-secret` | API secret for authentication | `--api-secret=YOUR_SECRET` |
| `--timeout` | Request timeout in seconds (default: 30) | `--timeout=60` |
| `--pretty` | Pretty print JSON output (default: true) | `--pretty=false` |
| `--help`, `-h` | Show help message | `python cli.py --help` |

### Scripting Examples

The CLI is perfect for shell scripts and automation:

```bash
#!/bin/bash
# Monitor BTC price every 30 seconds

export COINDCX_API_KEY="your_key"
export COINDCX_API_SECRET="your_secret"

while true; do
  echo "Checking BTC price at $(date)"
  python cli.py get_orderbook --pair=KC-BTC_USDT | jq -r '.asks | keys[0]'
  sleep 30
done
```

```bash
#!/bin/bash
# Get account balances and filter non-zero balances

python cli.py get_balances | jq '.[] | select((.balance | tonumber) > 0)'
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
    pair='KC-BTC_USDT',
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

**Futures Public Endpoints:**
- `get_futures_candles(pair, from_time, to_time, resolution)` - Get futures candlestick data
- `get_active_instruments(margin_currency_short_name)` - Get list of active futures instruments
- `get_instrument_details(pair, margin_currency_short_name)` - Get detailed instrument information
- `get_futures_trade_history(pair)` - Get real-time trade history for futures

**Authenticated Endpoints:**
- `get_balances()` - Get account balances
- `get_user_info()` - Get user information

**Spot Trading:**
- `create_spot_order(market, side, order_type, total_quantity, ...)` - Create spot orders (market/limit)

**Futures Trading:**
- `create_futures_order(pair, side, order_type, total_quantity, ...)` - Create futures orders (market/limit/stop/take-profit)
- `list_futures_orders(side, status, ...)` - List futures orders filtering by status
- `edit_futures_order(id, total_quantity, price, ...)` - Edit open futures orders

### 🚧 Coming Soon

**Spot Trading:**
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
- Cancel futures order
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
coindcx-python/
├── coindcx/
│   ├── __init__.py
│   ├── client.py          # Main Client class
│   ├── exceptions.py      # Custom exceptions
│   ├── enums.py          # Enums and constants
│   └── endpoints/        # Modular endpoint implementations
│       ├── __init__.py
│       ├── market.py     # Public market endpoints
│       ├── spot.py       # Spot trading
│       ├── margin.py     # Margin trading
│       └── futures.py    # Futures trading
├── examples/
│   └── basic_usage.py
├── cli.py                # Command-line interface tool
├── setup.py
├── requirements.txt
└── README.md
```

### Running Examples

```bash
# Set your API credentials as environment variables (optional)
export COINDCX_API_KEY="your_api_key"
export COINDCX_API_SECRET="your_api_secret"

# Run Python examples
python examples/basic_usage.py
python examples/futures_instruments.py  # Futures instruments example

# Or use the CLI tool for quick testing
python cli.py get_markets
python cli.py get_ticker
python cli.py get_balances  # Requires API credentials
python cli.py get_active_instruments --margin_currency_short_name=USDT
python cli.py get_instrument_details --pair=B-BTC_USDT
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

### v0.2.0 (2024-12-XX)
- **NEW:** Spot order creation - `create_spot_order()` for spot trading
  - Support for market and limit orders
  - Optional client order ID tracking
  - Comprehensive parameter validation
- **NEW:** Futures order creation - `create_futures_order()` for futures trading
  - Support for all futures order types: market, limit, stop-limit, stop-market, take-profit-limit, take-profit-market
  - Advanced features: leverage control, take profit/stop loss, time-in-force options
  - Post-only orders and hidden orders support
  - Isolated/crossed margin support
- **NEW:** Futures order management
  - `list_futures_orders()` - List orders with status filters
  - `edit_futures_order()` - Edit open order quantity, price, and TP/SL triggers
- **ENHANCED:** CLI tool now supports order creation commands
- **ENHANCED:** Documentation with comprehensive trading examples
- **ENHANCED:** Better error handling for order validation

### v0.1.0 (2024-01-XX)
- Initial release
- Support for public market data endpoints
- Support for basic authenticated endpoints
- HMAC-SHA256 signature generation
- Comprehensive error handling
- Generic CLI tool with automatic method discovery
- Futures endpoints support

---

# Development Notes

## How to prepare markdown documentation

1. Copy HTML from https://docs.coindcx.com/ to ai/coindcx_documentation.html
2. Run 

````bash
make
````

OR

````bash
html-to-markdown ai/coindcx_documentation.html -o ai/coindcx_documentation.md
````
