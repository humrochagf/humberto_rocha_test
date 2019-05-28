#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md') as fd:
    README = fd.read()

setup(
    name='chronos',
    version='1.0.0',
    description='Geo Distributed LRU (Least Recently Used) cache library',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Humberto Rocha',
    author_email='humrochagf@gmail',
    py_modules=['chronos'],
    platforms='any',
    install_requires=['pendulum==2.0.4'],
)
