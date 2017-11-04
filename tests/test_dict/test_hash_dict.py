"""Testing dict-related utiliti functions of the strct package."""

import pytest

from strct.dicts import hash_dict


def test_simple_dict():
    """Tests hash_dict with a shallow dict."""
    dict1 = {'a': 4, 8: 'b'}
    dict2 = {8: 'b', 'a': 4}
    assert hash_dict(dict1) == hash_dict(dict1)
    assert hash_dict(dict1) == hash_dict(dict2)


def test_deep_dict():
    """Tests hash_dict with a nested dict."""
    dict1 = {'a': 4, 3: {'b': 9, True: 'e'}}
    dict2 = {3: {True: 'e', 'b': 9}, 'a': 4}
    assert hash_dict(dict1) == hash_dict(dict1)
    assert hash_dict(dict1) == hash_dict(dict2)


def test_unhashable_val():
    """Tests hash_dict with a nested dict."""
    dict1 = {'a': [1, 2], 4: 'b'}
    dict2 = {4: 'b', 'a': [1, 2]}
    with pytest.raises(ValueError):
        assert hash_dict(dict1) == hash_dict(dict2)
