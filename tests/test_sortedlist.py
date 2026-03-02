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


def test_find_range_ix_in_section_list():
    """Testing the find_range_ix_in_section_list function."""
    seclist = SortedList([5, 8, 30, 31])
    assert find_range_ix_in_section_list(3, 4, seclist) == [0, 0]
    assert find_range_ix_in_section_list(6, 7, seclist) == [0, 1]
    assert find_range_ix_in_section_list(7, 9, seclist) == [0, 2]
    assert find_range_ix_in_section_list(7, 30, seclist) == [0, 3]
    assert find_range_ix_in_section_list(7, 321, seclist) == [0, 3]
    assert find_range_ix_in_section_list(4, 321, seclist) == [0, 3]


def test_find_range_in_section_list():
    """Testing the find_range_in_section_list function."""
    seclist = SortedList([5, 8, 30, 31])
    assert find_range_in_section_list(3, 4, seclist) == []
    assert find_range_in_section_list(6, 7, seclist) == [5]
    assert find_range_in_section_list(7, 9, seclist) == [5, 8]
    assert find_range_in_section_list(7, 30, seclist) == [5, 8, 30]
    assert find_range_in_section_list(7, 321, seclist) == [5, 8, 30]
    assert find_range_in_section_list(4, 321, seclist) == [5, 8, 30]


def test_find_range_ix_in_point_list():
    """Testing the find_range_ix_in_point_list function."""
    point_list = SortedList([5, 8, 15])
    assert find_range_ix_in_point_list(3, 4, point_list) == [0, 0]
    assert find_range_ix_in_point_list(3, 7, point_list) == [0, 1]
    assert find_range_ix_in_point_list(3, 8, point_list) == [0, 2]
    assert find_range_ix_in_point_list(4, 15, point_list) == [0, 3]
    assert find_range_ix_in_point_list(4, 321, point_list) == [0, 3]
    assert find_range_ix_in_point_list(6, 321, point_list) == [1, 3]

