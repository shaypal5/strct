"""Testing some dict-related strct functions."""

from strct.dicts import (
    increment_dict_val,
    increment_nested_val,
)


def get_dict_1():
    return {
        'a': 1,
        'b': 2,
    }


def get_nested_dict_1():
    return {
        'a': 1,
        'b': {
            'g': 2,
        },
    }


def test_increment_dict_val():
    dic1 = get_dict_1()
    increment_dict_val(dic1, 'a', 1)
    assert dic1['a'] == 2
    increment_dict_val(dic1, 'c', 4)
    assert dic1['c'] == 4


def test_increment_nested_val():
    dic1 = get_nested_dict_1()
    increment_nested_val(dic1, ('a'), 1)
    assert dic1['a'] == 2
    increment_nested_val(dic1, ('c'), 3)
    assert dic1['c'] == 3
    increment_nested_val(dic1, ('b', 'g'), 4)
    assert dic1['b']['g'] == 6
    increment_nested_val(dic1, ('b', 'z'), 17)
    assert dic1['b']['z'] == 17
