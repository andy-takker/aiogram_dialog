#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from os import path

from setuptools import setup, find_packages

this_directory = path.abspath(path.dirname(__file__))


setup(
    name='aiogram_dialog',
    description='Mini-framework for dialogs on top of aiogram',
    version='2.0.0b9',
    url='https://github.com/tishka17/aiogram_dialog',
    author='A. Tikhonov',
    author_email='17@itishka.org',
    license='Apache2',
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3'
    ],
    packages=find_packages(include=['aiogram_dialog', 'aiogram_dialog.*']),
    install_requires=[
        'aiogram>=3.0.0b4,<4.0.0',
        'jinja2',
        'cachetools==4.*',
        'magic_filter',
    ],
    extras_require={
        "tools": [
            "diagrams"
        ]
    },
    package_data={
        'aiogram_dialog.tools': ['calculator.png'],
        'aiogram_dialog.tools.templates': ['message.html'],
    },
    python_requires=">=3.8",
)
