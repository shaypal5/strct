"""sortedlist-related utility functions."""

from .sortedlist import (
    # sorted lists
    find_point_in_section_list,
    find_range_ix_in_section_list,
    find_range_in_section_list,
    find_range_ix_in_point_list
)
try:
    del sortedlist
except NameError:
    pass
