from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PAYMENT_STATUS_UNSPECIFIED: _ClassVar[PaymentStatus]
    PAYMENT_STATUS_PROCESSING: _ClassVar[PaymentStatus]
    PAYMENT_STATUS_SUCCEEDED: _ClassVar[PaymentStatus]
    PAYMENT_STATUS_FAILED: _ClassVar[PaymentStatus]
    PAYMENT_STATUS_CANCELLED: _ClassVar[PaymentStatus]
PAYMENT_STATUS_UNSPECIFIED: PaymentStatus
PAYMENT_STATUS_PROCESSING: PaymentStatus
PAYMENT_STATUS_SUCCEEDED: PaymentStatus
PAYMENT_STATUS_FAILED: PaymentStatus
PAYMENT_STATUS_CANCELLED: PaymentStatus

class CreatePaymentRequest(_message.Message):
    __slots__ = ("booking_id", "user_id", "amount_minor", "currency", "idempotency_key", "correlation_id")
    BOOKING_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_MINOR_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_ID_FIELD_NUMBER: _ClassVar[int]
    booking_id: str
    user_id: str
    amount_minor: int
    currency: str
    idempotency_key: str
    correlation_id: str
    def __init__(self, booking_id: _Optional[str] = ..., user_id: _Optional[str] = ..., amount_minor: _Optional[int] = ..., currency: _Optional[str] = ..., idempotency_key: _Optional[str] = ..., correlation_id: _Optional[str] = ...) -> None: ...

class CreatePaymentResponse(_message.Message):
    __slots__ = ("payment_id", "status")
    PAYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    payment_id: str
    status: PaymentStatus
    def __init__(self, payment_id: _Optional[str] = ..., status: _Optional[_Union[PaymentStatus, str]] = ...) -> None: ...

class GetPaymentRequest(_message.Message):
    __slots__ = ("payment_id", "correlation_id")
    PAYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    CORRELATION_ID_FIELD_NUMBER: _ClassVar[int]
    payment_id: str
    correlation_id: str
    def __init__(self, payment_id: _Optional[str] = ..., correlation_id: _Optional[str] = ...) -> None: ...

class GetPaymentResponse(_message.Message):
    __slots__ = ("payment_id", "booking_id", "user_id", "amount_minor", "currency", "status")
    PAYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    BOOKING_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_MINOR_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    payment_id: str
    booking_id: str
    user_id: str
    amount_minor: int
    currency: str
    status: PaymentStatus
    def __init__(self, payment_id: _Optional[str] = ..., booking_id: _Optional[str] = ..., user_id: _Optional[str] = ..., amount_minor: _Optional[int] = ..., currency: _Optional[str] = ..., status: _Optional[_Union[PaymentStatus, str]] = ...) -> None: ...
