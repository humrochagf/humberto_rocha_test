# Chronos 🕐

Geo Distributed LRU (Least Recently Used) cache library.

This code was written and tested with python 3.7.

## Naming

The library comes from [Chronos](https://en.wikipedia.org/wiki/Chronos) the
personification of time.


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

```python
from chronos import Chronos

chronos = Chronos(max_size=2)

chronos.set('key1', 'value1')
chronos.set('key2', 'value2')
chronos.set('key3', 'value3')

chronos.get('key3')
'value3'

chronos.get('key1')
None
```

## Running the tests

To run the tests use:

```shell
pytest tests.py
```
