"""Testing the threadsafe_generator decorator."""

from sortedcontainers import SortedList

from strct.sortedlists import (  # noqa: F401
    find_point_in_section_list,
    find_range_in_section_list,
    find_range_ix_in_point_list,
    find_range_ix_in_section_list,
)


def test_find_point_in_section_list():
    """Testing the find_point_in_section_list function."""
    seclist = SortedList([5, 8, 30, 31])
    assert find_point_in_section_list(4, seclist) is None
    assert find_point_in_section_list(5, seclist) == 5
    assert find_point_in_section_list(27, seclist) == 8
    assert find_point_in_section_list(31, seclist)
