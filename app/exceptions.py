class ValidationError(Exception):
    """Raised when validation fails in the service layer."""
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class NotFoundError(Exception):
    """Raised when a requested resource is not found."""
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class DatabaseError(Exception):
    """Raised for database-related issues."""
    def __init__(self, message):
        self.message = message
        super().__init__(message)
