class BaseException(Exception):
    """Base class for all exceptions in the application."""
    pass

class NotFoundException(BaseException):
    """Exception raised when a resource is not found."""
    def __init__(self, message: str = "Not found", status_code: int = 404):
        self.message = message
        self.status_code = status_code
        super().__init__(message)

class ValidationException(BaseException):
    """Exception raised for validation errors."""
    def __init__(self, message: str = "Validation error", status_code: int = 422):
        self.message = message
        self.status_code = status_code
        super().__init__(message)