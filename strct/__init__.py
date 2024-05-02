"""Utility pure-Python 3 decorators."""

import strct.dicts
import strct.hash
import strct.lists
import strct.sets
import strct.sortedlists

from ._version import *  # noqa: F403

try:
    del strct
except NameError:  # pragma: no cover
    pass
