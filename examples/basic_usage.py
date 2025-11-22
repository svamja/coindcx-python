"""
Basic usage examples for CoinDCX Python API

This script demonstrates:
1. Public endpoints (no authentication required)
2. Authenticated endpoints (requires API key/secret)
3. Error handling
"""

import os
from coindcx import (
    Client,
    CoinDCXAPIException,
    CoinDCXAuthenticationException,
    CandleInterval,
)


def public_endpoints_example():
    """Examples of public endpoints that don't require authentication"""
    print("=" * 60)
    print("PUBLIC ENDPOINTS EXAMPLE")
    print("=" * 60)

    # Initialize client without credentials
    client = Client()

    # Get all available markets
    print("\n1. Getting all markets...")
    try:
        markets = client.get_markets()
        print(f"   ✓ Found {len(markets)} markets")
        print(f"   First 5 markets: {markets[:5]}")
    except CoinDCXAPIException as e:
        print(f"   ✗ Error: {e}")

    # Get ticker for all markets
    print("\n2. Getting ticker data...")
    try:
        tickers = client.get_ticker()
        print(f"   ✓ Received ticker for {len(tickers)} markets")
        # Show first 3 tickers
        for ticker in tickers[:3]:
            print(f"   {ticker['market']}: {ticker['last_price']} (24h change: {ticker.get('change_24_hour', 'N/A')}%)")
    except CoinDCXAPIException as e:
        print(f"   ✗ Error: {e}")

    # Get market details
    print("\n3. Getting market details...")
    try:
        details = client.get_markets_details()
        print(f"   ✓ Received details for {len(details)} markets")
        # Show details for one market
        if details:
            market = details[0]
            print(f"   Example: {market['coindcx_name']}")
            print(f"   - Min quantity: {market['min_quantity']}")
            print(f"   - Max quantity: {market['max_quantity']}")
            print(f"   - Min price: {market['min_price']}")
            print(f"   - Max price: {market['max_price']}")
    except CoinDCXAPIException as e:
        print(f"   ✗ Error: {e}")

    # Get order book for a specific pair
    print("\n4. Getting order book for B-BTC_USDT...")
    try:
        orderbook = client.get_orderbook('B-BTC_USDT')
        bids = orderbook.get('bids', {})
        asks = orderbook.get('asks', {})
        if bids and asks:
            best_bid = list(bids.keys())[0]
            best_ask = list(asks.keys())[0]
            print(f"   ✓ Order book retrieved")
            print(f"   Best bid: {best_bid} ({bids[best_bid]} BTC)")
            print(f"   Best ask: {best_ask} ({asks[best_ask]} BTC)")
            spread = float(best_ask) - float(best_bid)
            print(f"   Spread: {spread:.2f} USDT")
    except CoinDCXAPIException as e:
        print(f"   ✗ Error: {e}")

    # Get recent trades
    print("\n5. Getting recent trades for B-BTC_USDT...")
    try:
        trades = client.get_trades('B-BTC_USDT', limit=5)
        print(f"   ✓ Retrieved {len(trades)} recent trades")
        for i, trade in enumerate(trades[:3], 1):
            print(f"   {i}. Price: {trade['p']}, Quantity: {trade['q']}")
    except CoinDCXAPIException as e:
        print(f"   ✗ Error: {e}")

    # Get candlestick data
    print("\n6. Getting candlestick data (1 hour intervals)...")
    try:
        candles = client.get_candles(
            pair='B-BTC_USDT',
            interval=CandleInterval.ONE_HOUR,
            limit=24  # Last 24 hours
        )
        print(f"   ✓ Retrieved {len(candles)} candles")
        if candles:
            latest = candles[0]
            print(f"   Latest candle:")
            print(f"   - Open: {latest['open']}")
            print(f"   - High: {latest['high']}")
            print(f"   - Low: {latest['low']}")
            print(f"   - Close: {latest['close']}")
            print(f"   - Volume: {latest['volume']}")
    except CoinDCXAPIException as e:
        print(f"   ✗ Error: {e}")

    # Close the client
    client.close()


def authenticated_endpoints_example():
    """Examples of authenticated endpoints that require API credentials"""
    print("\n\n" + "=" * 60)
    print("AUTHENTICATED ENDPOINTS EXAMPLE")
    print("=" * 60)

    # Get credentials from environment variables
    api_key = os.getenv('COINDCX_API_KEY')
    api_secret = os.getenv('COINDCX_API_SECRET')

    if not api_key or not api_secret:
        print("\n⚠️  API credentials not found in environment variables")
        print("   Set COINDCX_API_KEY and COINDCX_API_SECRET to run this example")
        print("\n   Example:")
        print("   export COINDCX_API_KEY='your_api_key'")
        print("   export COINDCX_API_SECRET='your_api_secret'")
        return

    # Initialize client with credentials
    client = Client(api_key=api_key, api_secret=api_secret)

    # Get account balances
    print("\n1. Getting account balances...")
    try:
        balances = client.get_balances()
        print(f"   ✓ Retrieved balances for {len(balances)} currencies")

        # Show balances with non-zero amounts
        non_zero = [b for b in balances if float(b['balance']) > 0 or float(b.get('locked_balance', 0)) > 0]
        if non_zero:
            print(f"   Non-zero balances ({len(non_zero)}):")
            for balance in non_zero[:5]:  # Show first 5
                available = balance['balance']
                locked = balance.get('locked_balance', 0)
                currency = balance['currency']
                print(f"   - {currency}: {available} (locked: {locked})")
        else:
            print("   No non-zero balances found")
    except CoinDCXAuthenticationException as e:
        print(f"   ✗ Authentication Error: {e}")
    except CoinDCXAPIException as e:
        print(f"   ✗ API Error: {e}")

    # Get user info
    print("\n2. Getting user information...")
    try:
        user_info = client.get_user_info()
        print(f"   ✓ User information retrieved")
        print(f"   - User ID: {user_info['coindcx_id']}")
        print(f"   - Email: {user_info['email']}")
        print(f"   - Name: {user_info.get('first_name', '')} {user_info.get('last_name', '')}")
    except CoinDCXAuthenticationException as e:
        print(f"   ✗ Authentication Error: {e}")
    except CoinDCXAPIException as e:
        print(f"   ✗ API Error: {e}")

    # Close the client
    client.close()


def context_manager_example():
    """Example using context manager for automatic resource cleanup"""
    print("\n\n" + "=" * 60)
    print("CONTEXT MANAGER EXAMPLE")
    print("=" * 60)

    print("\nUsing 'with' statement for automatic cleanup...")

    # Public endpoint with context manager
    with Client() as client:
        markets = client.get_markets()
        print(f"   ✓ Retrieved {len(markets)} markets")
        print("   ✓ Client session will be automatically closed")

    print("   ✓ Context manager exited, session closed")


def error_handling_example():
    """Examples of error handling"""
    print("\n\n" + "=" * 60)
    print("ERROR HANDLING EXAMPLE")
    print("=" * 60)

    client = Client()

    # Example 1: Trying to call authenticated endpoint without credentials
    print("\n1. Attempting authenticated call without credentials...")
    try:
        balances = client.get_balances()
    except CoinDCXAuthenticationException as e:
        print(f"   ✓ Caught expected error: {e}")

    # Example 2: Invalid market pair
    print("\n2. Attempting to get orderbook for invalid market...")
    try:
        orderbook = client.get_orderbook('INVALID_MARKET_PAIR')
    except CoinDCXAPIException as e:
        print(f"   ✓ Caught API error: {e}")
        if e.status_code:
            print(f"   Status code: {e.status_code}")

    client.close()


if __name__ == "__main__":
    print("\n" + "█" * 60)
    print("█" + " " * 58 + "█")
    print("█" + " " * 15 + "CoinDCX Python API Demo" + " " * 20 + "█")
    print("█" + " " * 58 + "█")
    print("█" * 60)

    # Run examples
    public_endpoints_example()
    authenticated_endpoints_example()
    context_manager_example()
    error_handling_example()

    print("\n\n" + "=" * 60)
    print("DEMO COMPLETED")
    print("=" * 60)
    print("\nFor more information, see:")
    print("- README.md for full documentation")
    print("- https://docs.coindcx.com for API reference")
    print()
