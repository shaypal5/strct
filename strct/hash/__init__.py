"""General data-structure related utility functions."""

from ._hash import (
    stable_hash,
    json_based_stable_hash,
)
try:
    del _hash
except NameError:
    pass
