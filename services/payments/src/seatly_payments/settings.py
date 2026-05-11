from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class PaymentsSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    grpc_host: str = Field(default="0.0.0.0", validation_alias="PAYMENTS_GRPC_HOST")
    grpc_port: int = Field(default=50051, validation_alias="PAYMENTS_GRPC_PORT")
    log_level: str = Field(default="INFO", validation_alias="LOG_LEVEL")


@lru_cache
def get_payments_settings() -> PaymentsSettings:
    return PaymentsSettings()
