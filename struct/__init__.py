"""Utility pure-Python 3 decorators."""

import struct.dict
import struct.list
import struct.set
import struct.sortedlist
try:
    del struct
except NameError: # pragma: no cover
    pass

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
