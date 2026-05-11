from fastapi.testclient import TestClient

from seatly_booking.bootstrap.app_factory import create_app


def test_health_live_returns_ok() -> None:
    app = create_app()

    with TestClient(app) as client:
        response = client.get("/health/live")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "booking-service",
    }


def test_health_ready_returns_ok() -> None:
    app = create_app()

    with TestClient(app) as client:
        response = client.get("/health/ready")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "booking-service",
    }


def test_request_context_headers_are_returned() -> None:
    app = create_app()

    with TestClient(app) as client:
        response = client.get(
            "/health/live",
            headers={
                "x-request-id": "request-1",
                "x-correlation-id": "correlation-1",
            },
        )

    assert response.status_code == 200
    assert response.headers["x-request-id"] == "request-1"
    assert response.headers["x-correlation-id"] == "correlation-1"


def test_request_context_headers_are_generated_when_missing() -> None:
    app = create_app()

    with TestClient(app) as client:
        response = client.get("/health/live")

    assert response.status_code == 200
    assert response.headers["x-request-id"]
    assert response.headers["x-correlation-id"]
