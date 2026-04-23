# mathlib

A Python package with two arithmetic helpers: `add` and `multiply`.
Both functions accept `int` or `float` operands.

## Install

```bash
# From the repo root — installs the package in editable mode
pip install -e ".[dev]"
```

## Usage

```python
from mathlib import add, multiply

add(2, 3)        # 5
multiply(2.5, 4) # 10.0
```

## Run the tests

```bash
pytest
```

All 10 tests must pass with no skips.

## Lint

```bash
ruff check .
```
