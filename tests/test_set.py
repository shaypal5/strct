"""Testing set related utility functions."""

from strct.sets import get_priority_elem_in_set


def test_get_priority_elem_in_set():
    """Basic test of the get_priority_elem_in_set function."""
    obj_set = {3, 2, 7, 8}
    priority_list = [4, 8, 1, 3]
    assert get_priority_elem_in_set(obj_set, priority_list) == 8


def test_get_priority_elem_in_set_no_match():
    """Test get_priority_elem_in_set returns None when no match found."""
    obj_set = {3, 2, 7, 8}
    priority_list = [4, 9, 10]
    assert get_priority_elem_in_set(obj_set, priority_list) is None
