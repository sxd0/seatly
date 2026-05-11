import uvicorn
from fastapi import FastAPI

from seatly_booking.bootstrap.app_factory import create_app as build_app
from seatly_booking.platform.config import get_booking_settings


def create_app() -> FastAPI:
    return build_app()


def main() -> None:
    settings = get_booking_settings()

    uvicorn.run(
        "seatly_booking.apps.api.main:create_app",
        factory=True,
        host=settings.http_host,
        port=settings.http_port,
        reload=settings.debug,
    )


if __name__ == "__main__":
    main()
