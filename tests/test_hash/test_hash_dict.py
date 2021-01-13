"""Testing dict-related utiliti functions of the strct package."""

from strct.hash import stable_hash


def test_simple_dict():
    """Tests stable_hash with a shallow dict."""
    dict1 = {'a': 4, 8: 'b'}
    dict2 = {8: 'b', 'a': 4}
    assert stable_hash(dict1) == stable_hash(dict1)
    assert stable_hash(dict1) == stable_hash(dict2)


def test_deep_dict():
    """Tests stable_hash with a nested dict."""
    dict1 = {'a': 4, 3: {'b': 9, True: 'e'}}
    dict2 = {3: {True: 'e', 'b': 9}, 'a': 4}
    assert stable_hash(dict1) == stable_hash(dict1)
    assert stable_hash(dict1) == stable_hash(dict2)


def test_unhashable_val():
    """Tests stable_hash with a nested dict."""
    dict1 = {'a': [1, 2], 4: 'b'}
    dict2 = {4: 'b', 'a': [1, 2]}
    assert stable_hash(dict1) == stable_hash(dict2)
