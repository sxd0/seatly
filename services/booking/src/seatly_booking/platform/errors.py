from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ErrorDetails:
    code: str
    message: str


class ApplicationError(Exception):
    status_code = 500
    code = "internal_error"
    message = "Internal server error"

    def details(self) -> ErrorDetails:
        return ErrorDetails(
            code=self.code,
            message=self.message,
        )


class NotFoundError(ApplicationError):
    status_code = 404
    code = "not_found"
    message = "Resource not found"


class ConflictError(ApplicationError):
    status_code = 409
    code = "conflict"
    message = "Resource conflict"


class UnauthorizedError(ApplicationError):
    status_code = 401
    code = "unauthorized"
    message = "Unauthorized"


class ForbiddenError(ApplicationError):
    status_code = 403
    code = "forbidden"
    message = "Forbidden"


class ValidationApplicationError(ApplicationError):
    status_code = 422
    code = "validation_error"
    message = "Validation error"
