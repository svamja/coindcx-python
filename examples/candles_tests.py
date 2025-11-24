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

    # Get candlestick data
    print("\n6. Getting candlestick data (1 hour intervals)...")
    try:
        candles = client.get_candles(
            pair='KC-ETH_USDT',
            interval=CandleInterval.FIFTEEN_MINUTES,
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
        print(candles)
    except CoinDCXAPIException as e:
        print(f"   ✗ Error: {e}")

    # Close the client
    client.close()




if __name__ == "__main__":
    print("\n" + "█" * 60)
    print("█" + " " * 58 + "█")
    print("█" + " " * 15 + "CoinDCX Python API Demo" + " " * 20 + "█")
    print("█" + " " * 58 + "█")
    print("█" * 60)

    # Run examples
    public_endpoints_example()

    print("\n\n" + "=" * 60)
    print("DEMO COMPLETED")
    print("=" * 60)
    print("\nFor more information, see:")
    print("- README.md for full documentation")
    print("- https://docs.coindcx.com for API reference")
    print()
