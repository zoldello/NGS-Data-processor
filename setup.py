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
    # TODO(zoldello): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='ngs_genomic_coverage',
    version='0.1.0',
    description="Calculates genomic coverage from next-generation sequencing data stored in a CSV file",
    long_description=readme + '\n\n' + history,
    author="Audrey Roy Greenfeld",
    author_email='Philip Adenekan',
    url='https://github.com/zoldello/ngs_genomic_coverage',
    packages=find_packages(include=['ngs_genomic_coverage']),
    entry_points={
        'console_scripts': [
            'ngs_genomic_coverage=ngs_genomic_coverage.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='ngs_genomic_coverage',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
