.PHONY: sync test lint format build run clean

sync:
	uv sync

setup: sync
	uv run pre-commit install

test:
	uv run pytest

lint:
	uv run ruff check .

format:
	uv run ruff format .

format-check:
	uv run ruff format --check .

build:
	uv build --offline

check: lint format-check test build

run: build
	uv tool install --reinstall $(firstword $(wildcard dist/*.whl))
	algoflex

clean:
	rm -rf dist build *.egg-info .pytest_cache .ruff_cache