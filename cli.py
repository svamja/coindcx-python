#!/usr/bin/env python3
"""
Generic CLI for CoinDCX API Client

Usage:
    python cli.py [method_name] --arg1=value1 --arg2=value2

Examples:
    # Public endpoints (no auth required)
    python cli.py get_markets
    python cli.py get_ticker
    python cli.py get_trades --pair=KC-BTC_USDT --limit=10
    python cli.py get_orderbook --pair=KC-BTC_USDT
    python cli.py get_candles --pair=KC-BTC_USDT --interval=1h --limit=24

    # Authenticated endpoints (requires API credentials)
    python cli.py get_balances --api-key=YOUR_KEY --api-secret=YOUR_SECRET
    python cli.py get_user_info --api-key=YOUR_KEY --api-secret=YOUR_SECRET

    # Or use environment variables
    export COINDCX_API_KEY="your_key"
    export COINDCX_API_SECRET="your_secret"
    python cli.py get_balances

    # Futures endpoints
    python cli.py get_futures_candles --pair=B-BTC_USDT --from_time=1234567890 --to_time=1234567900 --resolution=1D
    python cli.py get_active_instruments --margin_currency_short_name=["USDT"]
    python cli.py get_active_instruments --margin_currency_short_name=USDT,INR
    python cli.py get_instrument_details --pair=B-BTC_USDT --margin_currency_short_name=USDT

Features:
    - Automatic method discovery from Client class
    - Type inference from method signatures
    - Support for environment variables (COINDCX_API_KEY, COINDCX_API_SECRET)
    - Pretty JSON output
    - Built-in help for all methods
"""

import sys
import os
import json
import inspect
from typing import get_type_hints, get_origin, get_args

try:
    from coindcx import Client
except ImportError:
    print("Error: coindcx module not found. Please install it first:")
    print("  pip install -e .")
    sys.exit(1)


def convert_value(value: str, expected_type):
    """
    Convert string value to expected type based on type hints

    Args:
        value: String value from CLI argument
        expected_type: Expected type from function signature

    Returns:
        Converted value in the appropriate type
    """
    # Handle Optional types (Optional[int] -> int | None)
    origin = get_origin(expected_type)
    if origin is type(None) or str(expected_type).startswith('typing.Optional'):
        # Extract the actual type from Optional
        args = get_args(expected_type)
        if args:
            expected_type = args[0]
            origin = get_origin(expected_type)

    # Handle list types (e.g., list, List[str])
    if expected_type == list or origin == list:
        # Try to parse as JSON first
        try:
            parsed = json.loads(value)
            if isinstance(parsed, list):
                return parsed
        except (json.JSONDecodeError, ValueError):
            pass

        # If not JSON, try to split by comma
        if ',' in value:
            return [item.strip() for item in value.split(',')]

        # Single item list
        return [value.strip()]

    # Handle basic types
    if expected_type == int or str(expected_type) == 'int':
        return int(value)
    elif expected_type == float or str(expected_type) == 'float':
        return float(value)
    elif expected_type == bool or str(expected_type) == 'bool':
        return value.lower() in ('true', '1', 'yes', 'y')
    else:
        return value


def get_client_methods():
    """
    Get all public methods from Client class that can be called via CLI

    Returns:
        Dictionary mapping method names to method objects
    """
    methods = {}
    for name, method in inspect.getmembers(Client, predicate=inspect.isfunction):
        # Skip private methods and special methods
        if name.startswith('_'):
            continue
        # Skip context manager methods
        if name in ('close', '__enter__', '__exit__'):
            continue
        methods[name] = method
    return methods


def get_method_info(method):
    """
    Extract information about a method including parameters and types

    Args:
        method: Method object to inspect

    Returns:
        Dictionary with method signature information
    """
    sig = inspect.signature(method)
    params = {}

    # Get type hints
    try:
        type_hints = get_type_hints(method)
    except:
        type_hints = {}

    for param_name, param in sig.parameters.items():
        # Skip 'self' parameter
        if param_name == 'self':
            continue

        param_info = {
            'required': param.default == inspect.Parameter.empty,
            'default': None if param.default == inspect.Parameter.empty else param.default,
            'type': type_hints.get(param_name, str),
        }
        params[param_name] = param_info

    return {
        'params': params,
        'doc': inspect.getdoc(method),
    }


def print_help(methods=None):
    """Print help message"""
    print(__doc__)
    print("\nAvailable methods:")
    print("-" * 80)

    if methods is None:
        methods = get_client_methods()

    for name in sorted(methods.keys()):
        method = methods[name]
        info = get_method_info(method)

        # Build parameter list
        params = []
        for param_name, param_info in info['params'].items():
            if param_info['required']:
                params.append(f"--{param_name}=<value>")
            else:
                default = param_info['default']
                params.append(f"[--{param_name}={default}]")

        params_str = ' '.join(params)
        print(f"\n  {name} {params_str}")

        # Print first line of docstring
        if info['doc']:
            first_line = info['doc'].split('\n')[0].strip()
            print(f"    {first_line}")

    print("\n" + "-" * 80)
    print("\nClient options:")
    print("  --api-key=<key>        API key (or set COINDCX_API_KEY env var)")
    print("  --api-secret=<secret>  API secret (or set COINDCX_API_SECRET env var)")
    print("  --timeout=<seconds>    Request timeout (default: 30)")
    print("  --pretty               Pretty print JSON output (default: true)")
    print("  --help, -h             Show this help message")
    print()


def parse_args(args):
    """
    Parse command line arguments in the format --key=value

    Args:
        args: List of command line arguments

    Returns:
        Tuple of (method_name, method_args_dict, client_options_dict)
    """
    if not args or args[0] in ('--help', '-h', 'help'):
        print_help()
        sys.exit(0)

    method_name = args[0]
    method_args = {}
    client_options = {
        'api_key': os.getenv('COINDCX_API_KEY'),
        'api_secret': os.getenv('COINDCX_API_SECRET'),
        'timeout': 30,
        'pretty': True,
    }

    # Parse remaining arguments
    for arg in args[1:]:
        if not arg.startswith('--'):
            print(f"Error: Invalid argument format: {arg}")
            print("Arguments must be in the format: --key=value")
            sys.exit(1)

        if '=' not in arg:
            print(f"Error: Invalid argument format: {arg}")
            print("Arguments must be in the format: --key=value")
            sys.exit(1)

        key, value = arg[2:].split('=', 1)

        # Handle client options
        if key in ('api-key', 'api_key'):
            client_options['api_key'] = value
        elif key in ('api-secret', 'api_secret'):
            client_options['api_secret'] = value
        elif key == 'timeout':
            client_options['timeout'] = int(value)
        elif key == 'pretty':
            client_options['pretty'] = value.lower() in ('true', '1', 'yes', 'y')
        else:
            # Method argument
            method_args[key] = value

    return method_name, method_args, client_options


def main():
    """Main CLI entry point"""
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    # Get available methods
    methods = get_client_methods()

    # Parse arguments
    method_name, method_args, client_options = parse_args(sys.argv[1:])

    # Check if method exists
    if method_name not in methods:
        print(f"Error: Unknown method '{method_name}'")
        print(f"\nAvailable methods: {', '.join(sorted(methods.keys()))}")
        print("\nRun 'python cli.py --help' for more information")
        sys.exit(1)

    # Get method info
    method = methods[method_name]
    method_info = get_method_info(method)

    # Convert and validate arguments
    converted_args = {}
    for param_name, param_info in method_info['params'].items():
        if param_name in method_args:
            # Convert the argument to the expected type
            try:
                converted_args[param_name] = convert_value(
                    method_args[param_name],
                    param_info['type']
                )
            except (ValueError, TypeError) as e:
                print(f"Error: Invalid value for parameter '{param_name}': {method_args[param_name]}")
                print(f"Expected type: {param_info['type']}")
                sys.exit(1)
        elif param_info['required']:
            print(f"Error: Missing required parameter: --{param_name}")
            print(f"\nUsage: python cli.py {method_name}", end='')
            for pname, pinfo in method_info['params'].items():
                if pinfo['required']:
                    print(f" --{pname}=<value>", end='')
                else:
                    print(f" [--{pname}={pinfo['default']}]", end='')
            print()
            sys.exit(1)

    # Create client
    try:
        client = Client(
            api_key=client_options['api_key'],
            api_secret=client_options['api_secret'],
            timeout=client_options['timeout'],
        )
    except Exception as e:
        print(f"Error: Failed to initialize client: {e}")
        sys.exit(1)

    # Call the method
    try:
        result = getattr(client, method_name)(**converted_args)

        # Print result
        if client_options['pretty']:
            print(json.dumps(result, indent=2))
        else:
            print(json.dumps(result))

        # Clean up
        client.close()

    except Exception as e:
        print(f"Error: {type(e).__name__}: {e}", file=sys.stderr)
        client.close()
        sys.exit(1)


if __name__ == '__main__':
    main()
