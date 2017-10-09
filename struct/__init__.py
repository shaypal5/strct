"""Utility pure-Python 3 decorators."""

import structura.dict
import structura.list
import structura.set
import structura.sortedlist
try:
    del structura
except NameError: # pragma: no cover
    pass

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
