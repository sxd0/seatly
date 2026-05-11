import asyncio
import logging
from collections.abc import Callable
from typing import cast

import grpc

from seatly_common.contracts.payments.v1 import payments_pb2_grpc
from seatly_payments.application.payment_service import PaymentApplicationService
from seatly_payments.presentation.grpc.payment_servicer import PaymentGrpcServicer
from seatly_payments.settings import get_payments_settings

logger = logging.getLogger(__name__)


async def serve() -> None:
    settings = get_payments_settings()

    logging.basicConfig(
        level=settings.log_level,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )

    payment_service = PaymentApplicationService()
    payment_servicer = PaymentGrpcServicer(payment_service)

    server = grpc.aio.server()

    register_payment_servicer = cast(
        Callable[[payments_pb2_grpc.PaymentServiceServicer, grpc.aio.Server], None],
        payments_pb2_grpc.add_PaymentServiceServicer_to_server,
    )
    register_payment_servicer(payment_servicer, server)

    listen_address = f"{settings.grpc_host}:{settings.grpc_port}"
    server.add_insecure_port(listen_address)

    await server.start()

    logger.info("payments gRPC server started on %s", listen_address)

    try:
        await server.wait_for_termination()
    except asyncio.CancelledError:
        logger.info("payments gRPC server shutdown requested")
        raise
    finally:
        logger.info("payments gRPC server stopping")
        await asyncio.shield(server.stop(grace=5))
        logger.info("payments gRPC server stopped")


def main() -> None:
    try:
        asyncio.run(serve())
    except KeyboardInterrupt:
        logger.info("payments gRPC server interrupted")


if __name__ == "__main__":
    main()
