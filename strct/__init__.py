"""Utility pure-Python 3 decorators."""

from . import dicts
from . import lists
from . import sets
from . import sortedlists
from . import general
#import strct.dict
#import strct.list
#import strct.set
#import strct.sortedlist
#import strct.general

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

try:
    del strct
except NameError: # pragma: no cover
    pass
