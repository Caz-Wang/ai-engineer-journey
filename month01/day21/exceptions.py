class PostServiceError(Exception):
    """Base exception for post service errors."""


class PostNotFoundError(PostServiceError):
    """Raised when a requested post cannot be found."""


class ApiError(PostServiceError):
    """Raised when an API request fails."""