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
    entry_points={
        'console_scripts': [
            'chronos=chronos:cli'
        ],
    },
    platforms='any',
    install_requires=[
        'Click==7.0',
        'pendulum==2.0.4',
    ],
)
