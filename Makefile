# Get absolute path of project root
PYTHONPATH := $(shell pwd)

# === Test Commands ===

# Run all tests using pytest
test:
	PYTHONPATH=$(PYTHONPATH) python3 -m pytest tests

# Run a specific test file: make test-file file=tests/data/test_tokenizer.py
test-file:
	PYTHONPATH=$(PYTHONPATH) python3 $(file)

# === Code Quality ===

# Check style with Ruff
lint:
	ruff textpipe tests

# Auto-format with Ruff
format:
	ruff format textpipe tests

# === Documentation ===

# Build Sphinx documentation
docs:
	sphinx-build -b html docs docs/_build/html

# === Cleaning ===

# Clean all build and cache files
clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -r {} +
	find . -type d -name '.pytest_cache' -exec rm -r {} +
	find . -type d -name '.mypy_cache' -exec rm -r {} +
	find . -type d -name '.ruff_cache' -exec rm -r {} +
	find . -type d -name 'docs/_build' -exec rm -r {} +
	find . -type d -name 'build' -exec rm -r {} +
	find . -type d -name 'dist' -exec rm -r {} +
	find . -type d -name '*.egg-info' -exec rm -r {} +
	find . -type f \( -name '*.log' -o -name '.coverage' -o -name '*.pdb' \) -delete

.PHONY: test test-file lint format docs clean
