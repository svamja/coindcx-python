"""
CoinDCX API Exceptions
"""


class CoinDCXException(Exception):
    """Base exception for CoinDCX API"""

    def __init__(self, message, status_code=None, response=None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.response = response

    def __str__(self):
        if self.status_code:
            return f"[{self.status_code}] {self.message}"
        return self.message


class CoinDCXAPIException(CoinDCXException):
    """Exception for API errors returned by CoinDCX"""
    pass


class CoinDCXRequestException(CoinDCXException):
    """Exception for request errors (network, timeout, etc.)"""
    pass


class CoinDCXAuthenticationException(CoinDCXException):
    """Exception for authentication errors"""
    pass


class CoinDCXRateLimitException(CoinDCXException):
    """Exception for rate limit errors"""
    pass


class CoinDCXOrderException(CoinDCXException):
    """Exception for order-related errors"""
    pass


class CoinDCXInvalidOrderException(CoinDCXOrderException):
    """Exception for invalid order parameters"""
    pass
