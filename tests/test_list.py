"""Testing list-related utility functions."""

from strct.lists import (
    all_but,
    order_preserving_single_element_shift,
    order_preserving_single_index_shift,
)


def test_all_but():
    arr = [12, 34, 5, 54]
    assert all_but(arr, 2) == [12, 34, 54]
    assert all_but(arr, 0) == [34, 5, 54]
    assert all_but(arr, 3) == [12, 34, 5]


def test_order_preserving_single_index_shift():
    arr = ["a", "b", "c", "d"]
    assert order_preserving_single_index_shift(arr, 2, 0) == ["c", "a", "b", "d"]
    assert order_preserving_single_index_shift(arr, 2, 3) == ["a", "b", "d", "c"]
    assert order_preserving_single_index_shift(arr, 0, 2) == ["b", "c", "a", "d"]
    assert order_preserving_single_index_shift(arr, 3, 1) == ["a", "d", "b", "c"]


def test_order_preserving_single_element_shift():
    arr = ["a", "b", "c", "d"]
    assert order_preserving_single_element_shift(arr, "c", 0) == [
        "c",
        "a",
        "b",
        "d",
    ]
