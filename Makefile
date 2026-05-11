PYTHON ?= python
PIP ?= $(PYTHON) -m pip

.PHONY: venv install format lint typecheck test check clean

venv:
	$(PYTHON) -m venv venv

install:
	$(PIP) install --upgrade pip
	$(PIP) install -e ".[dev]"

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

clean:
	rm -rf .pytest_cache .ruff_cache .mypy_cache htmlcov .coverage coverage.xml
	find . -type d -name "__pycache__" -prune -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
