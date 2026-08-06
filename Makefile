.PHONY: sync test lint format build run clean

sync: 
	uv sync 

test: 
	uv run pytest 

lint:
	uv run ruff check . 

format:
	uv run ruff format . 

build:
	uv build --offline 

run: build 
	uv tool install --reinstall $(firstword $(wildcard dist/*.whl))
	algoflex 

clean:
	rm -rf dist build *.egg-info .pytest_cache .ruff_cache 