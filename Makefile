.PHONY: sync test lint format build run clean help

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

help:
	@echo "\n    make setup\n       - set up algoflex development enviroment, install packages and pre-commit hooks"
	@echo "\n    make test\n       - run tests"
	@echo "\n    make lint\n       - check for linting errors"
	@echo "\n    make format\n       - check for formatting issues"
	@echo "\n    make build\n       - build the project"
	@echo "\n    make run\n       - build and launch algoflex"
