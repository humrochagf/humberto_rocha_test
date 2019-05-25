# Themis ⚖️

This library is designed to determine whether a version number
is greater than, equal, or less than the other

This code was written and tested with python 3.7.

## Naming

The naming for this solution came from the [ancient Greek Titaness named Themis](https://en.wikipedia.org/wiki/Themis).
She is the personification of the divine order and her symbols are the Scales of Justice.


## Environment

Prepare a new environment to install the packages without polluting your system

```shell
python3 -m venv .env
source .env/bin/activate
pip install -r requirements-dev.txt
```

## Intalling the library

To install the library at your system run:

```shell
pip install .
```

## Usage

You can compare versions by using the `cmp_version` function:

```python
from themis import cmp_version

cmp_version('1.1', '1.0')
1
cmp_version('1.1', '1.1')
0
cmp_version('1.1', '1.2')
-1
```

## Running the tests

To run the tests use:

```shell
pytest tests.py
```
