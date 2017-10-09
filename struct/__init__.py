"""Utility pure-Python 3 decorators."""

import strct.dict
import strct.list
import strct.set
import strct.sortedlist
try:
    del strct
except NameError: # pragma: no cover
    pass

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
