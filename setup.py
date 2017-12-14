#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

setup_requirements = [
    'pytest-runner',
    # TODO(granitosaurus): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: put package test requirements here
]

setup(
    name='coinbitrage',
    version='0.1.1',
    description="Arbitrage estimator for crypto currency exchanges",
    long_description=readme + '\n\n' + history,
    author="Bernardas Ališauskas",
    author_email='bernardas.alisauskas@protonmail.com',
    url='https://github.com/granitosaurus/coinbitrage',
    packages=find_packages(include=['coinbitrage']),
    entry_points={
        'console_scripts': [
            'coinbitrage=coinbitrage.main:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='coinbitrage',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
