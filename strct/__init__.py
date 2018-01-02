"""Utility pure-Python 3 decorators."""

import strct.dicts
import strct.lists
import strct.sets
import strct.sortedlists
import strct.hash

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

try:
    del strct
except NameError: # pragma: no cover
    pass
