from dataclasses import dataclass
from enum import StrEnum
from uuid import uuid4


class PaymentStatus(StrEnum):
    PROCESSING = "processing"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELLED = "cancelled"


@dataclass(frozen=True, slots=True)
class CreatePaymentCommand:
    booking_id: str
    user_id: str
    amount_minor: int
    currency: str
    idempotency_key: str
    correlation_id: str


@dataclass(frozen=True, slots=True)
class PaymentDTO:
    payment_id: str
    booking_id: str
    user_id: str
    amount_minor: int
    currency: str
    status: PaymentStatus


class PaymentApplicationService:
    def __init__(self) -> None:
        self._payments: dict[str, PaymentDTO] = {}

    async def create_payment(self, command: CreatePaymentCommand) -> PaymentDTO:
        payment = PaymentDTO(
            payment_id=str(uuid4()),
            booking_id=command.booking_id,
            user_id=command.user_id,
            amount_minor=command.amount_minor,
            currency=command.currency,
            status=PaymentStatus.PROCESSING,
        )

        self._payments[payment.payment_id] = payment

        return payment

    async def get_payment(self, payment_id: str) -> PaymentDTO | None:
        return self._payments.get(payment_id)
