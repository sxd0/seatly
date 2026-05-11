from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class BookingSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    environment: str = Field(default="local", validation_alias="APP_ENV")
    debug: bool = Field(default=True, validation_alias="APP_DEBUG")

    service_name: str = Field(default="booking-service", validation_alias="BOOKING_SERVICE_NAME")
    http_host: str = Field(default="0.0.0.0", validation_alias="BOOKING_HTTP_HOST")
    http_port: int = Field(default=8000, validation_alias="BOOKING_HTTP_PORT")

    log_level: str = Field(default="INFO", validation_alias="LOG_LEVEL")


@lru_cache
def get_booking_settings() -> BookingSettings:
    return BookingSettings()
