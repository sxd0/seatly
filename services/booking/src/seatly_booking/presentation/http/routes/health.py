from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel

from seatly_booking.platform.config import get_booking_settings

router = APIRouter(prefix="/health", tags=["health"])


class HealthResponse(BaseModel):
    status: Literal["ok"]
    service: str


@router.get("/live", response_model=HealthResponse)
async def live() -> HealthResponse:
    settings = get_booking_settings()

    return HealthResponse(
        status="ok",
        service=settings.service_name,
    )


@router.get("/ready", response_model=HealthResponse)
async def ready() -> HealthResponse:
    settings = get_booking_settings()

    return HealthResponse(
        status="ok",
        service=settings.service_name,
    )
