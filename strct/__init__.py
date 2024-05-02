"""Utility pure-Python 3 decorators."""

# ruff: noqa

import strct.dicts
import strct.hash
import strct.lists
import strct.sets
import strct.sortedlists

from ._version import *  # noqa: F403

from contextlib import suppress
with suppress(NameError):
    del strct
