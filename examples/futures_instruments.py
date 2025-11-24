"""
Example script demonstrating futures instruments endpoints

This script shows how to:
1. Get list of active futures instruments
2. Get detailed information about specific instruments
"""

from coindcx import Client


def main():
    # Initialize client (no authentication needed for these public endpoints)
    client = Client()

    print("=" * 60)
    print("FUTURES INSTRUMENTS EXAMPLE")
    print("=" * 60)

    # Example 1: Get all USDT margined active instruments
    print("\n1. Getting USDT margined active instruments...")
    usdt_instruments = client.get_active_instruments(['USDT'])
    print(f"   Total USDT instruments: {len(usdt_instruments)}")
    print(f"   First 5 instruments: {usdt_instruments[:5]}")

    # Example 2: Get INR margined active instruments
    print("\n2. Getting INR margined active instruments...")
    inr_instruments = client.get_active_instruments(['INR'])
    print(f"   Total INR instruments: {len(inr_instruments)}")
    print(f"   First 5 instruments: {inr_instruments[:5]}")

    # Example 3: Get both USDT and INR margined instruments
    print("\n3. Getting all active instruments (USDT + INR)...")
    all_instruments = client.get_active_instruments(['USDT', 'INR'])
    print(f"   Total instruments: {len(all_instruments)}")

    # Example 4: Get detailed information for BTC USDT futures
    if usdt_instruments:
        # Use first instrument from the list
        btc_pair = 'B-BTC_USDT' if 'B-BTC_USDT' in usdt_instruments else usdt_instruments[0]
        print(f"\n4. Getting detailed information for {btc_pair}...")

        details = client.get_instrument_details(btc_pair, 'USDT')
        instrument = details['instrument']

        print(f"\n   Instrument Details for {btc_pair}:")
        print(f"   ├─ Status: {instrument['status']}")
        print(f"   ├─ Type: {instrument['kind']}")
        print(f"   ├─ Settlement: {instrument['settlement']}")
        print(f"   ├─ Max Leverage (Long): {instrument['max_leverage_long']}x")
        print(f"   ├─ Max Leverage (Short): {instrument['max_leverage_short']}x")
        print(f"   ├─ Price Increment: {instrument['price_increment']}")
        print(f"   ├─ Quantity Increment: {instrument['quantity_increment']}")
        print(f"   ├─ Min Quantity: {instrument['min_quantity']}")
        print(f"   ├─ Max Quantity: {instrument['max_quantity']}")
        print(f"   ├─ Min Notional: {instrument['min_notional']}")
        print(f"   ├─ Maker Fee: {instrument['maker_fee']}%")
        print(f"   ├─ Taker Fee: {instrument['taker_fee']}%")
        print(f"   ├─ Funding Frequency: Every {instrument['funding_frequency']} hours")
        print(f"   ├─ Order Types: {', '.join(instrument['order_types'])}")
        print(f"   └─ Time in Force: {', '.join(instrument['time_in_force_options'])}")

        print(f"\n   Dynamic Leverage Limits:")
        for leverage, size in instrument['dynamic_position_leverage_details'].items():
            print(f"   └─ {leverage}x leverage: Max position ${size:,.0f}")

    # Example 5: Compare different instruments
    print("\n5. Comparing multiple instruments...")
    sample_pairs = [p for p in usdt_instruments[:3]]  # Get first 3 pairs

    print(f"\n   Comparing: {', '.join(sample_pairs)}")
    print(f"\n   {'Pair':<20} {'Max Leverage':<15} {'Maker Fee':<12} {'Taker Fee':<12}")
    print(f"   {'-'*60}")

    for pair in sample_pairs:
        try:
            details = client.get_instrument_details(pair, 'USDT')
            inst = details['instrument']
            print(f"   {pair:<20} {inst['max_leverage_long']:<15} {inst['maker_fee']:<12} {inst['taker_fee']:<12}")
        except Exception as e:
            print(f"   {pair:<20} Error: {str(e)}")

    print("\n" + "=" * 60)
    print("Example completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
