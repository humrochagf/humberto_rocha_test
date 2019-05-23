# Eclipse 🌒

This program takes two lines at the x-axis and determine if they overlap.

This code was written and tested with python 3.7.

## Naming

The naming for this solution came from the eclipse itself where the moon "overlaps"
the sun, or the sun "overlaps" the moon.

## Environment

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
