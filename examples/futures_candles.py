"""
Futures Candles Example for CoinDCX Python API

This script demonstrates how to fetch futures candlestick data.
"""

import time
from datetime import datetime, timedelta
from coindcx import (
    Client,
    FuturesResolution,
    CoinDCXAPIException,
)


def get_futures_candles_example():
    """Example of getting futures candlestick data"""
    print("=" * 60)
    print("FUTURES CANDLES EXAMPLE")
    print("=" * 60)

    # Initialize client (no authentication required for public endpoint)
    client = Client()

    # Calculate time range (last 7 days)
    to_time = int(time.time())
    from_time = to_time - (7 * 24 * 60 * 60)  # 7 days ago

    print(f"\nFetching BTC futures candles...")
    print(f"From: {datetime.fromtimestamp(from_time).strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"To: {datetime.fromtimestamp(to_time).strftime('%Y-%m-%d %H:%M:%S')}")

    try:
        # Get 1-day candles for BTC futures
        candles = client.get_futures_candles(
            pair='B-BTC_USDT',
            from_time=from_time,
            to_time=to_time,
            resolution=FuturesResolution.ONE_DAY
        )

        print(f"\n✓ Status: {candles['s']}")
        print(f"✓ Retrieved {len(candles['data'])} candles\n")

        # Display candle data
        print("Candle Data:")
        print("-" * 80)
        print(f"{'Date':<12} {'Open':>12} {'High':>12} {'Low':>12} {'Close':>12} {'Volume':>12}")
        print("-" * 80)

        for candle in candles['data'][-7:]:  # Show last 7 candles
            date = datetime.fromtimestamp(candle['time'] / 1000).strftime('%Y-%m-%d')
            print(
                f"{date:<12} "
                f"{candle['open']:>12.2f} "
                f"{candle['high']:>12.2f} "
                f"{candle['low']:>12.2f} "
                f"{candle['close']:>12.2f} "
                f"{candle['volume']:>12.2f}"
            )

    except CoinDCXAPIException as e:
        print(f"\n✗ Error: {e}")
    finally:
        client.close()


def get_futures_candles_different_resolutions():
    """Example of fetching candles with different resolutions"""
    print("\n" + "=" * 60)
    print("DIFFERENT RESOLUTIONS EXAMPLE")
    print("=" * 60)

    client = Client()

    # Different time ranges for different resolutions
    resolutions = [
        (FuturesResolution.ONE_MINUTE, 60 * 60),       # Last 1 hour for 1min candles
        (FuturesResolution.FIVE_MINUTES, 5 * 60 * 60), # Last 5 hours for 5min candles
        (FuturesResolution.ONE_HOUR, 24 * 60 * 60),    # Last 24 hours for 1hour candles
        (FuturesResolution.ONE_DAY, 30 * 24 * 60 * 60) # Last 30 days for 1day candles
    ]

    for resolution, time_range in resolutions:
        to_time = int(time.time())
        from_time = to_time - time_range

        try:
            candles = client.get_futures_candles(
                pair='B-ETH_USDT',
                from_time=from_time,
                to_time=to_time,
                resolution=resolution
            )

            print(f"\n{resolution.name:20s}: {len(candles['data']):3d} candles")

            # Show first and last candle
            if candles['data']:
                first = candles['data'][0]
                last = candles['data'][-1]
                print(f"  First: ${first['open']:.2f} -> ${first['close']:.2f}")
                print(f"  Last:  ${last['open']:.2f} -> ${last['close']:.2f}")

        except CoinDCXAPIException as e:
            print(f"\n✗ Error for {resolution.name}: {e}")

    client.close()


def compare_spot_vs_futures():
    """Compare spot and futures candles for the same pair"""
    print("\n" + "=" * 60)
    print("SPOT VS FUTURES COMPARISON")
    print("=" * 60)

    client = Client()

    # Get last 24 hours
    to_time = int(time.time())
    from_time = to_time - (24 * 60 * 60)

    print("\nFetching BTC data for last 24 hours...")

    try:
        # Get futures candles (timestamps in seconds)
        futures_candles = client.get_futures_candles(
            pair='B-BTC_USDT',
            from_time=from_time,
            to_time=to_time,
            resolution=FuturesResolution.ONE_HOUR
        )

        # Get spot candles (timestamps in milliseconds)
        spot_candles = client.get_candles(
            pair='B-BTC_USDT',
            interval='1h',
            limit=24
        )

        print(f"\n✓ Futures candles: {len(futures_candles['data'])}")
        print(f"✓ Spot candles: {len(spot_candles)}")

        # Show latest prices
        if futures_candles['data']:
            latest_futures = futures_candles['data'][-1]
            print(f"\nLatest Futures Close: ${latest_futures['close']:.2f}")

        if spot_candles:
            latest_spot = spot_candles[0]
            print(f"Latest Spot Close: ${latest_spot['close']:.2f}")

        # Note the differences
        print("\n" + "-" * 60)
        print("KEY DIFFERENCES:")
        print("1. Futures uses timestamps in SECONDS")
        print("2. Futures resolution: '1', '5', '60', '1D'")
        print("3. Spot uses timestamps in MILLISECONDS")
        print("4. Spot interval: '1m', '5m', '1h', '1d'")
        print("5. Futures response has 's' (status) field")
        print("-" * 60)

    except CoinDCXAPIException as e:
        print(f"\n✗ Error: {e}")
    finally:
        client.close()


if __name__ == "__main__":
    print("\n" + "█" * 60)
    print("█" + " " * 58 + "█")
    print("█" + " " * 12 + "CoinDCX Futures Candles Demo" + " " * 17 + "█")
    print("█" + " " * 58 + "█")
    print("█" * 60)

    # Run examples
    get_futures_candles_example()
    get_futures_candles_different_resolutions()
    compare_spot_vs_futures()

    print("\n\n" + "=" * 60)
    print("DEMO COMPLETED")
    print("=" * 60)
    print("\nFor more information, see:")
    print("- README.md for full documentation")
    print("- https://docs.coindcx.com for API reference")
    print()
