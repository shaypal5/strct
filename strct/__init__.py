"""Utility pure-Python 3 decorators."""

from ._version import *  # noqa: F403

import strct.dicts
import strct.lists
import strct.sets
import strct.sortedlists
import strct.hash

try:
    del strct
except NameError: # pragma: no cover
    pass
