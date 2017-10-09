strct
#########
|PyPI-Status| |PyPI-Versions| |Build-Status| |Codecov| |LICENCE|

A small pure-python package for data strcture related utility functions.

.. code-block:: python

  from strct import lazy_property

  @lazy_property
  def paramless_big_calc():
    sub_res = [big_func(const) for const in array_of_constants]
    return sum(sub_res)

.. contents::

.. section-numbering::


Installation
============

Install ``strct`` with:

.. code-block:: bash

  pip install strct


Decorators
==========

lazy_property
-------------

The ``lazy_property`` decorator is meant to decorate functions that compute some constant value or property that you only want to compute once. The first call to the decorated function will run it and save the value (in memory) before returning it; subsequent calls will get this value without trigerring the calculation.

You can think about it like a ``functools.lru_cache(maxsize=1)`` for functions with no parameters.

.. code-block:: python

  from strct import lazy_property

  @lazy_property
  def paramless_big_calc():
    """I take a lot of time!"""
    sub_res = [big_func(const) for const in array_of_constants]
    return sum(sub_res)


threadsafe_generator
--------------------

The ``threadsafe_generator`` decorator makes generators threadsafe. This means multiple threads can be given references to the decorated generator and it is guarenteed that each item in the stream will be yielded (i.e. returned) to only a single thread.

.. code-block:: python

  from strct import threadsafe_generator

  @threadsafe_generator
  def user_documents(day):
    """I yield some MongoDB documents!"""
    client = get_mongodb_client(some_params)
    dt_obj = translate_day_to_dt(day)
    user_document_cursor = client.some_mongodb_query(dt_obj, SOME_CONST)
    while True:
      yield user_document_cursor.__next__()


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

  python -m pytest --cov=strct


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

.. |Build-Status| image:: https://travis-ci.org/shaypal5/strct.svg?branch=master
  :target: https://travis-ci.org/shaypal5/strct

.. |LICENCE| image:: https://img.shields.io/pypi/l/strct.svg
  :target: https://pypi.python.org/pypi/strct

.. |Codecov| image:: https://codecov.io/github/shaypal5/strct/coverage.svg?branch=master
   :target: https://codecov.io/github/shaypal5/strct?branch=master
