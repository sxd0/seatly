from typing import Any

from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel
from starlette.responses import JSONResponse

from seatly_booking.platform.context import get_correlation_id, get_request_id
from seatly_booking.platform.errors import ApplicationError


class ErrorResponse(BaseModel):
    code: str
    message: str
    request_id: str | None
    correlation_id: str | None
    details: Any | None = None


def build_error_response(
    *,
    code: str,
    message: str,
    details: Any | None = None,
) -> dict[str, Any]:
    error = ErrorResponse(
        code=code,
        message=message,
        request_id=get_request_id(),
        correlation_id=get_correlation_id(),
        details=details,
    )

    return {"error": jsonable_encoder(error.model_dump())}


async def application_error_handler(
    request: Request,
    exc: Exception,
) -> JSONResponse:
    if not isinstance(exc, ApplicationError):
        raise exc

    return JSONResponse(
        status_code=exc.status_code,
        content=build_error_response(
            code=exc.code,
            message=exc.message,
        ),
    )


async def validation_error_handler(
    request: Request,
    exc: Exception,
) -> JSONResponse:
    if not isinstance(exc, RequestValidationError):
        raise exc

    return JSONResponse(
        status_code=422,
        content=build_error_response(
            code="request_validation_error",
            message="Request validation error",
            details=exc.errors(),
        ),
    )


def register_error_handlers(app: FastAPI) -> None:
    app.add_exception_handler(ApplicationError, application_error_handler)
    app.add_exception_handler(RequestValidationError, validation_error_handler)
