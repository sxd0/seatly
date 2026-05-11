PYTHON ?= python
PIP ?= $(PYTHON) -m pip

PROTO_SRC_DIR := proto
PROTO_OUT_DIR := libs/common/src
PROTO_FILES := $(shell find $(PROTO_SRC_DIR) -name "*.proto")

.PHONY: venv install proto format lint typecheck test check run-payments-grpc clean

venv:
	$(PYTHON) -m venv venv

install:
	$(PIP) install --upgrade pip
	$(PIP) install -e ".[dev]"

proto:
	$(PYTHON) -m grpc_tools.protoc \
		-I$(PROTO_SRC_DIR) \
		--python_out=$(PROTO_OUT_DIR) \
		--grpc_python_out=$(PROTO_OUT_DIR) \
		--pyi_out=$(PROTO_OUT_DIR) \
		$(PROTO_FILES)
	find libs/common/src/seatly_common/contracts -type d -exec touch {}/__init__.py \;

format:
	ruff format .
	ruff check . --fix

lint:
	ruff format --check .
	ruff check .

typecheck:
	mypy libs services tests

test:
	pytest -q

check: lint typecheck test

run-payments-grpc:
	$(PYTHON) -m seatly_payments.apps.grpc.main

clean:
	rm -rf .pytest_cache .ruff_cache .mypy_cache htmlcov .coverage coverage.xml
	find . -type d -name "__pycache__" -prune -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
