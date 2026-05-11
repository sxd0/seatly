from seatly_payments.application.payment_service import (
    CreatePaymentCommand,
    PaymentApplicationService,
    PaymentStatus,
)


async def test_create_payment_returns_processing_payment() -> None:
    service = PaymentApplicationService()

    payment = await service.create_payment(
        CreatePaymentCommand(
            booking_id="booking-1",
            user_id="user-1",
            amount_minor=2500,
            currency="RUB",
            idempotency_key="key-1",
            correlation_id="correlation-1",
        )
    )

    assert payment.payment_id
    assert payment.booking_id == "booking-1"
    assert payment.user_id == "user-1"
    assert payment.amount_minor == 2500
    assert payment.currency == "RUB"
    assert payment.status == PaymentStatus.PROCESSING


async def test_get_payment_returns_existing_payment() -> None:
    service = PaymentApplicationService()

    created_payment = await service.create_payment(
        CreatePaymentCommand(
            booking_id="booking-1",
            user_id="user-1",
            amount_minor=2500,
            currency="RUB",
            idempotency_key="key-1",
            correlation_id="correlation-1",
        )
    )

    found_payment = await service.get_payment(created_payment.payment_id)

    assert found_payment == created_payment


async def test_get_payment_returns_none_for_missing_payment() -> None:
    service = PaymentApplicationService()

    found_payment = await service.get_payment("missing-payment")

    assert found_payment is None
