#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open('README.md') as fd:
    README = fd.read()

setup(
    name='themis',
    version='1.0.0',
    description=(
        'This library is designed to determine whether a version number '
        'is greater than, equal, or less than the other'
    ),
    long_description=README,
    long_description_content_type="text/markdown",
    author='Humberto Rocha',
    author_email='humrochagf@gmail',
    packages=find_packages(),
    platforms='any',
)
