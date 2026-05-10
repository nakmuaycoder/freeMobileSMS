.PHONY: install test lint format clean

install:
	uv venv
	uv pip install -e .
	uv pip install pytest pytest-cov requests pre-commit ruff detect-secrets
	.venv/bin/pre-commit install

test:
	uv run --extra dev pytest tests/

lint:
	uv run --extra dev ruff check .

format:
	uv run --extra dev ruff check --fix .
	uv run --extra dev ruff format .

scan-secrets:
	uv run --extra dev detect-secrets scan --baseline .secrets.baseline

clean:
	rm -rf .venv
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf *.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -f *.log
