from typing import override

import grpc

from seatly_common.contracts.payments.v1 import payments_pb2, payments_pb2_grpc
from seatly_payments.application.payment_service import (
    CreatePaymentCommand,
    PaymentApplicationService,
    PaymentDTO,
    PaymentStatus,
)


def payment_status_to_proto(status: PaymentStatus) -> payments_pb2.PaymentStatus:
    match status:
        case PaymentStatus.PROCESSING:
            return payments_pb2.PAYMENT_STATUS_PROCESSING
        case PaymentStatus.SUCCEEDED:
            return payments_pb2.PAYMENT_STATUS_SUCCEEDED
        case PaymentStatus.FAILED:
            return payments_pb2.PAYMENT_STATUS_FAILED
        case PaymentStatus.CANCELLED:
            return payments_pb2.PAYMENT_STATUS_CANCELLED


def payment_to_proto(payment: PaymentDTO) -> payments_pb2.GetPaymentResponse:
    return payments_pb2.GetPaymentResponse(
        payment_id=payment.payment_id,
        booking_id=payment.booking_id,
        user_id=payment.user_id,
        amount_minor=payment.amount_minor,
        currency=payment.currency,
        status=payment_status_to_proto(payment.status),
    )


class PaymentGrpcServicer(payments_pb2_grpc.PaymentServiceServicer):
    def __init__(self, payment_service: PaymentApplicationService) -> None:
        self._payment_service = payment_service

    @override
    async def CreatePayment(
        self,
        request: payments_pb2.CreatePaymentRequest,
        context: grpc.aio.ServicerContext,
    ) -> payments_pb2.CreatePaymentResponse:
        payment = await self._payment_service.create_payment(
            CreatePaymentCommand(
                booking_id=request.booking_id,
                user_id=request.user_id,
                amount_minor=request.amount_minor,
                currency=request.currency,
                idempotency_key=request.idempotency_key,
                correlation_id=request.correlation_id,
            )
        )

        return payments_pb2.CreatePaymentResponse(
            payment_id=payment.payment_id,
            status=payment_status_to_proto(payment.status),
        )

    @override
    async def GetPayment(
        self,
        request: payments_pb2.GetPaymentRequest,
        context: grpc.aio.ServicerContext,
    ) -> payments_pb2.GetPaymentResponse:
        payment = await self._payment_service.get_payment(request.payment_id)

        if payment is None:
            await context.abort(grpc.StatusCode.NOT_FOUND, "payment not found")
            raise RuntimeError("unreachable")

        return payment_to_proto(payment)
