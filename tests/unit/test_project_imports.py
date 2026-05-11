import seatly_booking
import seatly_common
import seatly_payments


def test_project_packages_are_importable() -> None:
    assert seatly_booking is not None
    assert seatly_common is not None
    assert seatly_payments is not None
