"""
Example usage of futures positions and exit position APIs

This example demonstrates:
1. Listing all futures positions
2. Getting positions filtered by pairs
3. Getting positions filtered by position IDs
4. Exiting a position
"""

from coindcx import Client
from coindcx.enums import OrderSide, FuturesOrderType
import os

# Initialize client with API credentials
api_key = os.getenv('COINDCX_API_KEY', 'your_api_key')
api_secret = os.getenv('COINDCX_API_SECRET', 'your_api_secret')

client = Client(api_key=api_key, api_secret=api_secret)


def list_all_positions():
    """List all futures positions"""
    print("\n=== List All Positions ===")
    try:
        # Get all USDT margined positions
        positions = client.list_positions(page=1, size=20)
        
        print(f"Total positions: {len(positions)}")
        for pos in positions:
            if pos['active_pos'] != 0:  # Only show active positions
                print(f"\nPair: {pos['pair']}")
                print(f"  Position ID: {pos['id']}")
                print(f"  Active Position: {pos['active_pos']}")
                print(f"  Average Price: {pos['avg_price']}")
                print(f"  Leverage: {pos['leverage']}x")
                print(f"  Margin Type: {pos['margin_type']}")
                print(f"  Locked Margin: {pos['locked_margin']}")
                print(f"  Liquidation Price: {pos['liquidation_price']}")
                if pos['take_profit_trigger']:
                    print(f"  Take Profit: {pos['take_profit_trigger']}")
                if pos['stop_loss_trigger']:
                    print(f"  Stop Loss: {pos['stop_loss_trigger']}")
    except Exception as e:
        print(f"Error listing positions: {e}")


def get_positions_by_pairs():
    """Get positions filtered by specific pairs"""
    print("\n=== Get Positions by Pairs ===")
    try:
        # Get positions for specific pairs
        pairs = 'B-BTC_USDT,B-ETH_USDT'
        positions = client.get_positions_by_filters(
            pairs=pairs,
            page=1,
            size=10
        )
        
        print(f"Positions for {pairs}:")
        for pos in positions:
            print(f"\n{pos['pair']}:")
            print(f"  Position ID: {pos['id']}")
            print(f"  Active Position: {pos['active_pos']}")
            print(f"  Average Price: {pos['avg_price']}")
            print(f"  Leverage: {pos['leverage']}x")
    except Exception as e:
        print(f"Error getting positions by pairs: {e}")


def get_position_by_id(position_id):
    """Get position by position ID"""
    print("\n=== Get Position by ID ===")
    try:
        positions = client.get_positions_by_filters(
            position_ids=position_id,
            page=1,
            size=1
        )
        
        if positions:
            pos = positions[0]
            print(f"Position Details:")
            print(f"  Pair: {pos['pair']}")
            print(f"  Position ID: {pos['id']}")
            print(f"  Active Position: {pos['active_pos']}")
            print(f"  Average Price: {pos['avg_price']}")
            print(f"  Leverage: {pos['leverage']}x")
            print(f"  Margin Type: {pos['margin_type']}")
            print(f"  Locked User Margin: {pos['locked_user_margin']}")
            print(f"  Maintenance Margin: {pos['maintenance_margin']}")
        else:
            print(f"No position found with ID: {position_id}")
    except Exception as e:
        print(f"Error getting position by ID: {e}")


def exit_position_example(position_id):
    """Exit a futures position"""
    print("\n=== Exit Position ===")
    try:
        # First, check the position exists and has an active position
        positions = client.get_positions_by_filters(position_ids=position_id)
        
        if not positions:
            print(f"No position found with ID: {position_id}")
            return
        
        pos = positions[0]
        print(f"Position to exit:")
        print(f"  Pair: {pos['pair']}")
        print(f"  Active Position: {pos['active_pos']}")
        
        if pos['active_pos'] == 0:
            print("  Position has no active quantity to exit")
            return
        
        # Exit the position
        print(f"\nExiting position {position_id}...")
        result = client.exit_position(position_id)
        
        print(f"Exit Status: {result['message']}")
        print(f"Status Code: {result['status']}")
        print(f"Group ID: {result['data']['group_id']}")
        print("\nNote: System may split large orders into smaller parts.")
        print("All parts will share the same group_id.")
        
    except Exception as e:
        print(f"Error exiting position: {e}")


def get_inr_positions():
    """Get INR margined positions"""
    print("\n=== Get INR Margined Positions ===")
    try:
        positions = client.list_positions(
            page=1,
            size=20,
            margin_currency_short_name=['INR']
        )
        
        print(f"Total INR positions: {len(positions)}")
        for pos in positions:
            if pos['active_pos'] != 0:
                print(f"\nPair: {pos['pair']}")
                print(f"  Active Position: {pos['active_pos']}")
                print(f"  Average Price: {pos['avg_price']}")
                print(f"  Settlement Currency Avg Price: {pos['settlement_currency_avg_price']}")
    except Exception as e:
        print(f"Error getting INR positions: {e}")


if __name__ == "__main__":
    print("CoinDCX Futures Positions API Examples")
    print("=" * 50)
    
    # Example 1: List all positions
    list_all_positions()
    
    # Example 2: Get positions by pairs
    get_positions_by_pairs()
    
    # Example 3: Get INR margined positions
    get_inr_positions()
    
    # Example 4: Get position by ID (replace with actual position ID)
    # Uncomment and replace with your actual position ID
    # get_position_by_id('your-position-id-here')
    
    # Example 5: Exit a position (BE CAREFUL - this will close your position!)
    # Uncomment and replace with actual position ID only if you want to exit
    # exit_position_example('your-position-id-here')
    
    print("\n" + "=" * 50)
    print("Examples completed!")
    print("\nNote: To use the exit_position example, uncomment the line")
    print("and provide your actual position ID. This will close the position!")
