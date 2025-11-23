"""
CoinDCX Futures Trading Endpoints

Endpoints for futures trading operations.
"""

from typing import Callable


class FuturesEndpoints:
    """
    Futures trading endpoints (requires authentication)

    Handles authenticated endpoints for futures trading including:
    - Create futures order
    - Cancel futures order
    - Get futures positions
    - Update leverage
    - Get futures transactions
    - Get futures order history

    Note: These endpoints are not yet implemented.
    """

    def __init__(self, request_handler: Callable):
        """
        Initialize futures trading endpoints

        Args:
            request_handler: Function to make authenticated HTTP requests (typically client._post)
        """
        self._post = request_handler

    # TODO: Implement futures trading endpoints
    # - create_futures_order()
    # - cancel_futures_order()
    # - get_futures_positions()
    # - update_leverage()
    # - get_futures_transactions()
    # - get_futures_order_history()
