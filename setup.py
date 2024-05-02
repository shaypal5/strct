# This file is part of strct.
# https://github.com/shaypal5/strct

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, Shay Palachy <shaypal5@gmail.com>
# Copyright (c) 2024, Jirka Borovec <***@gmail.com>

import os.path
from importlib.util import module_from_spec, spec_from_file_location

from pkg_resources import parse_requirements
from setuptools import find_packages, setup

_PATH_HERE = os.path.dirname(__file__)


def _load_py_module(fname: str):
    spec = spec_from_file_location(
        os.path.join("strct", fname),
        os.path.join(_PATH_HERE, "strct", fname),
    )
    py = module_from_spec(spec)
    spec.loader.exec_module(py)
    return py


with open(os.path.join(_PATH_HERE, "README.rst")) as fp:
    README_RST = fp.read()


_version = _load_py_module("_version.py")


def _load_requirements(
    path_dir: str = _PATH_HERE, file_name: str = "requirements.txt"
) -> list:
    with open(os.path.join(path_dir, file_name)) as fp:
        reqs = parse_requirements(fp.readlines())
    return list(map(str, reqs))


setup(
    name="strct",
    description=(
        "A small pure-python package for data structure related"
        "utility functions."
    ),
    long_description=README_RST,
    author="Shay Palachy Affek",
    author_email="shaypal5@gmail.com",
    version=_version.__version__,
    url="https://github.com/shaypal5/strct",
    license="MIT",
    packages=find_packages(exclude=["dist", "docs", "tests"]),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=_load_requirements(),
    platforms=["any"],
    keywords=["python", "list", "dict", "set", "sortedlist"],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Topic :: Other/Nonlisted Topic",
        "Intended Audience :: Developers",
    ],
)
