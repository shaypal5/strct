"""Setup for the strct package."""

# !/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import (
    setup,
    find_packages,
)

import versioneer


README_RST = ''
with open('README.rst') as f:
    README_RST = f.read()

INSTALL_REQUIRES = []
TEST_REQUIRES = ['sortedcontainers', 'pytest', 'coverage', 'pytest-cov']


setup(
    name='strct',
    description=("A small pure-python package for data structure related"
                 "utility functions."),
    long_description=README_RST,
    author="Shay Palachy",
    author_email="shaypal5@gmail.com",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    url='https://github.com/shaypal5/strct',
    license="MIT",
    packages=find_packages(exclude=['dist', 'docs', 'tests']),
    python_requires=">=3.4",
    install_requires=INSTALL_REQUIRES,
    extras_require={
        'test': TEST_REQUIRES
    },
    setup_requires=INSTALL_REQUIRES,
    platforms=['any'],
    keywords='python list dict set sortedlist',
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)
