from seatly_common.contracts.payments.v1 import payments_pb2, payments_pb2_grpc


def test_payments_grpc_contract_is_importable() -> None:
    assert payments_pb2.PAYMENT_STATUS_PROCESSING == 1
    assert payments_pb2.PAYMENT_STATUS_SUCCEEDED == 2
    assert payments_pb2_grpc.PaymentServiceStub is not None
