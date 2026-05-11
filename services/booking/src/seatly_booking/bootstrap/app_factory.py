from fastapi import FastAPI

from seatly_booking.platform.config import get_booking_settings
from seatly_booking.platform.logging import configure_logging
from seatly_booking.presentation.http.error_handlers import register_error_handlers
from seatly_booking.presentation.http.middleware import RequestContextMiddleware
from seatly_booking.presentation.http.router import api_router


def create_app() -> FastAPI:
    settings = get_booking_settings()

    configure_logging(settings.log_level)

    app = FastAPI(
        title=settings.service_name,
        debug=settings.debug,
        version="0.1.0",
    )

    app.add_middleware(RequestContextMiddleware)
    register_error_handlers(app)
    app.include_router(api_router)

    return app
