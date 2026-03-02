"""Test hash functions."""

import sys

from strct.hash import json_based_stable_hash, stable_hash


def test_stable_hash():
    if sys.version_info.major == 3:
        if sys.version_info.minor >= 6:
            expected_val = 5461671350068481966
        else:
            expected_val = -8814990287216496045
    else:
        raise Exception("This test is meant for Python 3!")
    listi = [3, 23.2, "23"]
    assert stable_hash(listi) == expected_val

    if sys.version_info.major == 3:
        if sys.version_info.minor >= 6:
            expected_val2 = -7233202952208267009
        else:
            expected_val2 = 4894511948741237771
    else:
        raise Exception("This test is meant for Python 3!")
    listi2 = [34, {"a": 23, "g": [1, "43"]}]
    assert stable_hash(listi2) == expected_val2

    if sys.version_info.major == 3:
        if sys.version_info.minor >= 6:
            expected_val3 = -1643351000552175288
        else:
            expected_val3 = -4531592806763782902
    else:
        raise Exception("This test is meant for Python 3!")
    dicti = {"a": 23, "b": [234, "g"], "c": {4: "go"}}
    assert stable_hash(dicti) == expected_val3


def test_stable_hash_complex():
    """Test stable_hash with a complex number."""
    assert stable_hash(complex(4, 5)) == 4


def test_stable_hash_float():
    """Test stable_hash with a float."""
    assert stable_hash(2.2) == 2


def test_stable_hash_unhashable_type():
    """Test stable_hash raises TypeError for truly unhashable primitives."""
    import pytest

    with pytest.raises(TypeError):
        stable_hash(object())


def test_stable_hash_dict_with_unhashable_val():
    """Test stable_hash raises TypeError for dicts with unhashable values."""
    import pytest

    with pytest.raises(TypeError):
        stable_hash({"a": object()})


def test_json_based_stable_hash():
    """Test json_based_stable_hash produces consistent results."""
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 2, "a": 1}
    assert json_based_stable_hash(dict1) == json_based_stable_hash(dict2)
    assert isinstance(json_based_stable_hash(dict1), str)

