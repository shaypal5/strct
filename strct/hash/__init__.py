"""General data-structure related utility functions."""

from ._hash import (
    json_based_stable_hash,
    stable_hash,
)

try:
    del _hash
except NameError:
    pass
