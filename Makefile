.PHONY: install test lint format clean

install:
	uv venv
	uv pip install -e .
	uv pip install pytest pytest-cov requests pre-commit ruff detect-secrets
	.venv/bin/pre-commit install

test:
	.venv/bin/pytest tests/

lint:
	.venv/bin/ruff check .

format:
	.venv/bin/ruff check --fix .
	.venv/bin/ruff format .

clean:
	rm -rf .venv
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf *.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -f *.log
