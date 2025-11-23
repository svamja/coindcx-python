"""
CoinDCX Spot Trading Endpoints

Endpoints for spot trading, account balances, and order management.
"""

from typing import Callable


class SpotEndpoints:
    """
    Spot trading endpoints (requires authentication)

    Handles authenticated endpoints for spot trading including:
    - Account balances
    - User information
    - Order creation and management (coming soon)
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
