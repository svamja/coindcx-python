# Futures Positions API Implementation

This document describes the newly implemented futures positions APIs for the CoinDCX Python client.

## Overview

Three new methods have been added to handle futures positions:

1. **`list_positions()`** - Get all futures positions
2. **`get_positions_by_filters()`** - Get positions filtered by pairs or position IDs
3. **`exit_position()`** - Exit a position by position ID

## API Reference

### 1. list_positions()

Get a paginated list of all futures positions.

**Signature:**
```python
client.list_positions(
    page: int = 1,
    size: int = 10,
    margin_currency_short_name: Optional[list] = None
) -> list
```

**Parameters:**
- `page` (int, optional): Page number. Default: 1
- `size` (int, optional): Number of records per page. Default: 10
- `margin_currency_short_name` (list, optional): List of margin currencies to filter by. 
  - Options: `['USDT']`, `['INR']`, or `['USDT', 'INR']`
  - Default: `['USDT']`

**Returns:**
List of position dictionaries with the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `id` | str | Position ID (permanent for each pair) |
| `pair` | str | Futures pair name (e.g., 'B-BTC_USDT') |
| `active_pos` | float | Quantity of position (negative for short) |
| `inactive_pos_buy` | float | Sum of open buy order quantities |
| `inactive_pos_sell` | float | Sum of open sell order quantities |
| `avg_price` | float | Average entry price |
| `liquidation_price` | float | Liquidation price (isolated margin only) |
| `locked_margin` | float | Margin locked after fees and funding |
| `locked_user_margin` | float | Initial margin invested |
| `locked_order_margin` | float | Margin locked in open orders |
| `take_profit_trigger` | float | Take profit trigger price |
| `stop_loss_trigger` | float | Stop loss trigger price |
| `leverage` | float | Position leverage |
| `maintenance_margin` | float | Minimum margin to avoid liquidation |
| `mark_price` | float | Mark price at last update (reference only) |
| `margin_type` | str | 'crossed' or 'isolated' |
| `settlement_currency_avg_price` | float | USDT<>INR conversion price (INR only) |
| `margin_currency_short_name` | str | Margin mode ('USDT' or 'INR') |
| `updated_at` | int | Timestamp of last position update |

**Example:**
```python
from coindcx import Client

client = Client(api_key='...', api_secret='...')

# Get all USDT margined positions
positions = client.list_positions(page=1, size=20)
for pos in positions:
    if pos['active_pos'] != 0:
        print(f"{pos['pair']}: {pos['active_pos']} @ {pos['avg_price']}")

# Get INR margined positions
inr_positions = client.list_positions(margin_currency_short_name=['INR'])

# Get both USDT and INR positions
all_positions = client.list_positions(margin_currency_short_name=['USDT', 'INR'])
```

**Notes:**
- All margin values are in USDT for INR Futures
- Position ID remains fixed for a particular pair over time
- For cross margined positions, maintenance margin is the sum of all positions

---

### 2. get_positions_by_filters()

Get futures positions filtered by specific pairs or position IDs.

**Signature:**
```python
client.get_positions_by_filters(
    page: int = 1,
    size: int = 10,
    pairs: Optional[str] = None,
    position_ids: Optional[str] = None,
    margin_currency_short_name: Optional[list] = None
) -> list
```

**Parameters:**
- `page` (int, optional): Page number. Default: 1
- `size` (int, optional): Number of records per page. Default: 10
- `pairs` (str, optional): Comma-separated list of instrument pairs
  - Example: `'B-BTC_USDT,B-ETH_USDT'`
- `position_ids` (str, optional): Comma-separated list of position IDs
  - Example: `'7830d2d6-0c3d-11ef-9b57-0fb0912383a7,id2,id3'`
- `margin_currency_short_name` (list, optional): List of margin currencies
  - Default: `['USDT']`

**Returns:**
List of position dictionaries (same format as `list_positions()`)

**Example:**
```python
from coindcx import Client

client = Client(api_key='...', api_secret='...')

# Get positions for specific pairs
btc_eth_positions = client.get_positions_by_filters(
    pairs='B-BTC_USDT,B-ETH_USDT'
)
for pos in btc_eth_positions:
    print(f"{pos['pair']}: Active {pos['active_pos']}")

# Get position by position ID
position = client.get_positions_by_filters(
    position_ids='7830d2d6-0c3d-11ef-9b57-0fb0912383a7'
)
print(f"Leverage: {position[0]['leverage']}x")

# Get multiple positions by IDs
positions = client.get_positions_by_filters(
    position_ids='id1,id2,id3',
    margin_currency_short_name=['USDT']
)
```

**Notes:**
- You must provide either `pairs` OR `position_ids`, not both
- Both parameters accept comma-separated values for multiple filters
- Position ID is obtained from `list_positions()` response

**Raises:**
- `CoinDCXInvalidOrderException`: If neither `pairs` nor `position_ids` is provided

---

### 3. exit_position()

Exit a futures position by creating a market order to close the entire position.

**Signature:**
```python
client.exit_position(position_id: str) -> dict
```

**Parameters:**
- `position_id` (str, required): Position ID to exit (obtained from `list_positions()`)

**Returns:**
Dictionary containing:
```python
{
    "message": "success",
    "status": 200,
    "code": 200,
    "data": {
        "group_id": "baf926e6B-ID_USDT1705647709"
    }
}
```

| Field | Description |
|-------|-------------|
| `message` | Success message |
| `status` | HTTP status code |
| `code` | Response code |
| `data.group_id` | ID used when large order is split. All parts share same group_id |

**Example:**
```python
from coindcx import Client

client = Client(api_key='...', api_secret='...')

# First, get your positions
positions = client.list_positions()
for pos in positions:
    if pos['active_pos'] != 0:
        print(f"{pos['pair']}: ID={pos['id']}")

# Exit a specific position
result = client.exit_position('434dc174-6503-4509-8b2b-71b325fe417a')
print(f"Status: {result['message']}")
print(f"Group ID: {result['data']['group_id']}")
```

**Notes:**
- This creates a market order to close the entire position
- System may auto-split large exit orders into smaller parts for better execution
- All split parts will share the same `group_id`
- Position ID is permanent for each pair and can be obtained from `list_positions()`
- **Warning:** This will immediately close your position. Use with caution!

---

## HTTP Endpoints

These methods map to the following CoinDCX API endpoints:

| Method | HTTP Endpoint |
|--------|--------------|
| `list_positions()` | `POST /exchange/v1/derivatives/futures/positions` |
| `get_positions_by_filters()` | `POST /exchange/v1/derivatives/futures/positions` |
| `exit_position()` | `POST /exchange/v1/derivatives/futures/positions/exit` |

All endpoints require authentication with API key and secret.

---

## Complete Example

See `examples/futures_positions.py` for a complete working example that demonstrates:

1. Listing all futures positions
2. Getting positions filtered by pairs
3. Getting positions filtered by position IDs
4. Exiting a position
5. Getting INR margined positions

To run the example:
```bash
export COINDCX_API_KEY='your_api_key'
export COINDCX_API_SECRET='your_api_secret'
python examples/futures_positions.py
```

---

## Error Handling

All methods may raise the following exceptions:

- `CoinDCXAuthenticationException`: If API credentials are not provided or invalid
- `CoinDCXAPIException`: For API-level errors (rate limits, invalid parameters, etc.)
- `CoinDCXInvalidOrderException`: For validation errors (e.g., missing required parameters)

Example with error handling:
```python
from coindcx import Client
from coindcx.exceptions import CoinDCXAPIException, CoinDCXAuthenticationException

client = Client(api_key='...', api_secret='...')

try:
    positions = client.list_positions()
    for pos in positions:
        print(f"{pos['pair']}: {pos['active_pos']}")
except CoinDCXAuthenticationException as e:
    print(f"Authentication error: {e}")
except CoinDCXAPIException as e:
    print(f"API error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

---

## Testing

A test script is provided in `examples/test_positions.py` to verify the implementation:

```bash
python examples/test_positions.py
```

This will verify that:
- All methods exist on the Client class
- All methods are callable
- Method signatures are correct
- Methods are properly integrated with the futures endpoints

---

## Implementation Details

### Files Modified

1. **`coindcx/endpoints/futures.py`**
   - Added `list_positions()` method
   - Added `get_positions_by_filters()` method
   - Added `exit_position()` method

2. **`coindcx/client.py`**
   - Added wrapper methods that delegate to futures endpoints
   - Maintained consistent API surface

### Files Created

1. **`examples/futures_positions.py`** - Complete usage examples
2. **`examples/test_positions.py`** - Integration tests
3. **`FUTURES_POSITIONS_API.md`** - This documentation

---

## API Reference Documentation

For complete API documentation, refer to:
- CoinDCX Official Documentation: https://docs.coindcx.com/
- Specific sections:
  - [List Positions](https://docs.coindcx.com/#list-positions)
  - [Get Positions By pairs or positionid](https://docs.coindcx.com/#get-positions-by-pairs-or-positionid)
  - [Exit Position](https://docs.coindcx.com/#exit-position)

---

## Support

For issues or questions:
1. Check the examples in `examples/futures_positions.py`
2. Refer to the CoinDCX official documentation
3. Open an issue on the GitHub repository
