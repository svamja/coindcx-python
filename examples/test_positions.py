"""
Simple test to verify the new positions APIs are properly integrated
"""

from coindcx import Client

# Test that methods exist and are callable
def test_methods_exist():
    """Verify that the new methods exist on the Client class"""
    
    # Initialize client (no credentials needed for this test)
    client = Client()
    
    # Check that methods exist
    assert hasattr(client, 'list_positions'), "list_positions method not found"
    assert hasattr(client, 'get_positions_by_filters'), "get_positions_by_filters method not found"
    assert hasattr(client, 'exit_position'), "exit_position method not found"
    
    # Check that methods are callable
    assert callable(client.list_positions), "list_positions is not callable"
    assert callable(client.get_positions_by_filters), "get_positions_by_filters is not callable"
    assert callable(client.exit_position), "exit_position is not callable"
    
    print("✓ All methods exist and are callable")


def test_futures_endpoints():
    """Verify that the futures endpoints class has the methods"""
    from coindcx.endpoints.futures import FuturesEndpoints
    
    # Check that the FuturesEndpoints class has the methods
    assert hasattr(FuturesEndpoints, 'list_positions'), "list_positions not found in FuturesEndpoints"
    assert hasattr(FuturesEndpoints, 'get_positions_by_filters'), "get_positions_by_filters not found in FuturesEndpoints"
    assert hasattr(FuturesEndpoints, 'exit_position'), "exit_position not found in FuturesEndpoints"
    
    print("✓ All methods exist in FuturesEndpoints")


def test_method_signatures():
    """Test that methods have correct signatures"""
    import inspect
    from coindcx import Client
    
    client = Client()
    
    # Check list_positions signature
    sig = inspect.signature(client.list_positions)
    params = list(sig.parameters.keys())
    assert 'page' in params, "list_positions missing 'page' parameter"
    assert 'size' in params, "list_positions missing 'size' parameter"
    assert 'margin_currency_short_name' in params, "list_positions missing 'margin_currency_short_name' parameter"
    print("✓ list_positions has correct signature")
    
    # Check get_positions_by_filters signature
    sig = inspect.signature(client.get_positions_by_filters)
    params = list(sig.parameters.keys())
    assert 'page' in params, "get_positions_by_filters missing 'page' parameter"
    assert 'size' in params, "get_positions_by_filters missing 'size' parameter"
    assert 'pairs' in params, "get_positions_by_filters missing 'pairs' parameter"
    assert 'position_ids' in params, "get_positions_by_filters missing 'position_ids' parameter"
    print("✓ get_positions_by_filters has correct signature")
    
    # Check exit_position signature
    sig = inspect.signature(client.exit_position)
    params = list(sig.parameters.keys())
    assert 'position_id' in params, "exit_position missing 'position_id' parameter"
    print("✓ exit_position has correct signature")


if __name__ == "__main__":
    print("Testing Futures Positions API Implementation")
    print("=" * 50)
    
    try:
        test_methods_exist()
        test_futures_endpoints()
        test_method_signatures()
        
        print("\n" + "=" * 50)
        print("✅ All tests passed!")
        print("\nThe following methods have been successfully implemented:")
        print("  1. list_positions() - Get all futures positions")
        print("  2. get_positions_by_filters() - Get positions by pairs or IDs")
        print("  3. exit_position() - Exit a position by position ID")
        print("\nSee examples/futures_positions.py for usage examples.")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        exit(1)
