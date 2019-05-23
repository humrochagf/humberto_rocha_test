# Eclipse 🌒

This program takes two lines at the x-axis and determine if they overlap.

This code was written and tested with python 3.7.

Prepare a new environment to install the packages without polluting your system

```shell
python3 -m venv .env
source .env/bin/activate
pip install -r requirements-dev.txt
```

## Running the tests

To run the tests use:

```shell
pytest tests.py
```

## Running the code

To run eclipse just run:

```shell
./eclipse.py
```

or

```shell
python3 eclipse.py
```

It will prompt you to enter each line, and the pattern for each line is `x1,x2`:

```
1,2
```
