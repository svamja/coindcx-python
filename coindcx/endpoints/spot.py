"""
CoinDCX Spot Trading Endpoints

Endpoints for spot trading, account balances, and order management.
"""

from typing import Callable, Union, Optional
from ..enums import OrderSide, OrderType
from ..exceptions import CoinDCXInvalidOrderException


class SpotEndpoints:
    """
    Spot trading endpoints (requires authentication)

    Handles authenticated endpoints for spot trading including:
    - Account balances
    - User information
    - Order creation and management
    - Trade history (coming soon)
    """

    def __init__(self, request_handler: Callable):
        """
        Initialize spot trading endpoints

        Args:
            request_handler: Function to make authenticated HTTP requests (typically client._post)
        """
        self._post = request_handler

    def get_balances(self) -> list:
        """
        Get account balances for all currencies

        Returns:
            List of balances for each currency

        Example:
            >>> client = Client(api_key='...', api_secret='...')
            >>> balances = client.get_balances()
            >>> for balance in balances:
            ...     print(f"{balance['currency']}: {balance['balance']}")

        Raises:
            CoinDCXAuthenticationException: If API credentials not provided
        """
        return self._post('/exchange/v1/users/balances')

    def get_user_info(self) -> dict:
        """
        Get user account information

        Returns:
            User information including ID, name, email, etc.

        Example:
            >>> client = Client(api_key='...', api_secret='...')
            >>> info = client.get_user_info()
            >>> print(info['email'])

        Raises:
            CoinDCXAuthenticationException: If API credentials not provided
        """
        return self._post('/exchange/v1/users/info')

    def create_order(
        self,
        market: str,
        side: Union[str, OrderSide],
        order_type: Union[str, OrderType],
        total_quantity: float,
        price_per_unit: Optional[float] = None,
        client_order_id: Optional[str] = None,
    ) -> dict:
        """
        Create a spot order

        Args:
            market: Market pair (e.g., 'KC-BTC_USDT', 'KC-ETH_USDT')
            side: Order side - 'buy' or 'sell' (or use OrderSide enum)
            order_type: Order type - 'market_order' or 'limit_order' (or use OrderType enum)
            total_quantity: Total quantity of base currency to buy/sell
            price_per_unit: Price per unit (required for limit orders)
            client_order_id: Optional client order ID for tracking

        Returns:
            Dictionary containing order details including:
                - id: Order ID
                - status: Order status
                - side: Order side
                - order_type: Order type
                - market: Market pair
                - total_quantity: Total quantity
                - remaining_quantity: Remaining quantity
                - avg_price: Average execution price
                - price_per_unit: Limit price (for limit orders)
                - created_at: Order creation timestamp
                - updated_at: Order update timestamp

        Raises:
            CoinDCXInvalidOrderException: If required parameters are missing or invalid
            CoinDCXAuthenticationException: If API credentials not provided
            CoinDCXAPIException: For API errors

        Example:
            >>> client = Client(api_key='...', api_secret='...')
            >>> # Create a limit buy order
            >>> order = client.create_spot_order(
            ...     market='KC-BTC_USDT',
            ...     side=OrderSide.BUY,
            ...     order_type=OrderType.LIMIT_ORDER,
            ...     total_quantity=0.001,
            ...     price_per_unit=50000
            ... )
            >>> print(f"Order ID: {order['id']}, Status: {order['status']}")
            >>>
            >>> # Create a market sell order
            >>> order = client.create_spot_order(
            ...     market='KC-BTC_USDT',
            ...     side='sell',
            ...     order_type='market_order',
            ...     total_quantity=0.001
            ... )

        Note:
            - Maximum of 25 open orders per market at a time
            - Rate limit: 2000 requests per 60 seconds
            - price_per_unit is required for limit orders
            - Use KC- prefix for spot market pairs
        """
        # Validate required parameters for limit orders
        if order_type in [OrderType.LIMIT_ORDER, "limit_order"] and price_per_unit is None:
            raise CoinDCXInvalidOrderException(
                "price_per_unit is required for limit orders"
            )

        # Build request body
        data = {
            "side": side.value if isinstance(side, OrderSide) else side,
            "order_type": order_type.value if isinstance(order_type, OrderType) else order_type,
            "market": market,
            "total_quantity": total_quantity,
        }

        if price_per_unit is not None:
            data["price_per_unit"] = price_per_unit

        if client_order_id is not None:
            data["client_order_id"] = client_order_id

        # Make request (timestamp added automatically by _post)
        response = self._post('/exchange/v1/orders/create', data=data)

        # Extract order from response
        if isinstance(response, dict) and 'orders' in response:
            return response['orders'][0] if response['orders'] else response

        return response
