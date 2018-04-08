"""Test the CaseInsensitiveDict class."""

from strct.dicts import CaseInsensitiveDict


REG_EXAMPLE = {'a': 4, 'C': {'g': 8, 2: 1}}


def test_base():
    dic = CaseInsensitiveDict()
    dic['a'] = 4
    dic[8] = 5
    assert dic['a'] == 4
    assert dic['A'] == 4
    assert dic[8] == 5


def test_from_dict():
    dic = CaseInsensitiveDict.from_dict(REG_EXAMPLE)
    assert dic['a'] == 4
    assert dic['A'] == 4
    assert dic['c']['G'] == 8
    assert dic['C'][2] == 1
