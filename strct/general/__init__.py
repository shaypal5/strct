"""General data-structure related utility functions."""

from ._general import (
    stable_hash_builtins_strct,
    hash_dict_list,
)
try:
    del _general
except NameError:
    pass
