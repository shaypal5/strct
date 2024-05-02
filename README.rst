strct
#####
|PyPI-Status| |PyPI-Versions| |Build-Status| |Codecov| |LICENCE|

A small pure-python package for data structure related utility functions.

.. code-block:: python

  from strct.dict import get_nested_val

  >>> dict_obj = {'a': {'b': 7}}
  >>> get_nested_val(('a', 'b'), dict_obj)
  7

.. contents::

.. section-numbering::


Installation
============

Install ``strct`` with:

.. code-block:: bash

  pip install strct


Use
===

``strct`` is divided into five sub-modules:

dicts
-----

Getting values from nested dicts in various ways; operations on number-valued dicts; merging, normalizing, reversing and printing dicts (nicely)


lists
-----

Index and element shifts that preserve order.


sets
----

Operations on sets:

- Getting a set element by a priority list.


sortedlists
-----------

Operations on ``sortedcontainers.SortedList`` objects.

hash
----

Provide cross-kernel stable hash functions that work for built-in data structures and types, and for any custom data structure complying with the iterable or dict schemes.


Contributing
============

Package author and current maintainer is Shay Palachy (shay.palachy@gmail.com); You are more than welcome to approach him for help. Contributions are very welcomed.

Installing for development
--------------------------

Clone:

.. code-block:: bash

  git clone git@github.com:shaypal5/strct.git


Install in development mode with test dependencies:

.. code-block:: bash

  cd strct
  pip install -e ".[test]"


Running the tests
-----------------

To run the tests, use:

.. code-block:: bash

  python -m pytest --cov=strct --doctest-modules


Adding documentation
--------------------

This project is documented using the `numpy docstring conventions`_, which were chosen as they are perhaps the most widely-spread conventions that are both supported by common tools such as Sphinx and result in human-readable docstrings (in my personal opinion, of course). When documenting code you add to this project, please follow `these conventions`_.

.. _`numpy docstring conventions`: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
.. _`these conventions`: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt


Credits
=======
Created by Shay Palachy  (shay.palachy@gmail.com).

.. |PyPI-Status| image:: https://img.shields.io/pypi/v/strct.svg
  :target: https://pypi.python.org/pypi/strct

.. |PyPI-Versions| image:: https://img.shields.io/pypi/pyversions/strct.svg
   :target: https://pypi.python.org/pypi/strct

.. |Build-Status| image:: https://github.com/shaypal5/strct/actions/workflows/test.yml/badge.svg
  :target: https://github.com/shaypal5/strct/actions/workflows/test.yml

.. |LICENCE| image:: https://img.shields.io/badge/License-MIT-yellow.svg
  :target: https://pypi.python.org/pypi/strct

.. |Codecov| image:: https://codecov.io/github/shaypal5/strct/coverage.svg?branch=master
   :target: https://codecov.io/github/shaypal5/strct?branch=master
