"""list-related utility functions."""

from ._list import (
    all_but,
    order_preserving_single_index_shift,
    order_preserving_single_element_shift,
)
try:
    del _list
except NameError:
    pass
