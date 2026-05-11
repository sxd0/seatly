from typing import cast

import grpc

from seatly_common.contracts.payments.v1 import payments_pb2
from seatly_payments.application.payment_service import PaymentApplicationService
from seatly_payments.presentation.grpc.payment_servicer import PaymentGrpcServicer


async def test_create_payment_grpc_returns_processing_status() -> None:
    application_service = PaymentApplicationService()
    servicer = PaymentGrpcServicer(application_service)

    response = await servicer.CreatePayment(
        payments_pb2.CreatePaymentRequest(
            booking_id="booking-1",
            user_id="user-1",
            amount_minor=2500,
            currency="RUB",
            idempotency_key="key-1",
            correlation_id="correlation-1",
        ),
        cast(grpc.aio.ServicerContext, None),
    )

    assert response.payment_id
    assert response.status == payments_pb2.PAYMENT_STATUS_PROCESSING


async def test_get_payment_grpc_returns_existing_payment() -> None:
    application_service = PaymentApplicationService()
    servicer = PaymentGrpcServicer(application_service)

    create_response = await servicer.CreatePayment(
        payments_pb2.CreatePaymentRequest(
            booking_id="booking-1",
            user_id="user-1",
            amount_minor=2500,
            currency="RUB",
            idempotency_key="key-1",
            correlation_id="correlation-1",
        ),
        cast(grpc.aio.ServicerContext, None),
    )

    get_response = await servicer.GetPayment(
        payments_pb2.GetPaymentRequest(
            payment_id=create_response.payment_id,
            correlation_id="correlation-1",
        ),
        cast(grpc.aio.ServicerContext, None),
    )

    assert get_response.payment_id == create_response.payment_id
    assert get_response.booking_id == "booking-1"
    assert get_response.user_id == "user-1"
    assert get_response.amount_minor == 2500
    assert get_response.currency == "RUB"
    assert get_response.status == payments_pb2.PAYMENT_STATUS_PROCESSING
