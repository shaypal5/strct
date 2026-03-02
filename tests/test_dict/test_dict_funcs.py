"""Testing some dict-related strct functions."""

import pytest

from strct.dicts import (
    add_many_to_dict_val_list,
    add_many_to_dict_val_set,
    add_to_dict_val_set,
    any_in_dict,
    any_path_in_dict,
    append_to_dict_val_list,
    deep_merge_dict,
    flatten_dict,
    get_alternative_nested_val,
    get_first_val,
    get_key_of_max,
    get_key_of_min,
    get_key_val_of_max,
    get_key_val_of_max_key,
    get_keys_of_max_n,
    get_nested_val,
    in_nested_dicts,
    increment_dict_val,
    increment_nested_val,
    key_tuple_value_nested_generator,
    key_value_nested_generator,
    norm_int_dict,
    pprint_dist_dict,
    pprint_int_dict,
    put_nested_val,
    reverse_dict,
    reverse_dict_partial,
    reverse_list_valued_dict,
    safe_alternative_nested_val,
    safe_nested_val,
    subdict_by_keys,
    sum_dicts,
    sum_num_dicts,
    unite_dicts,
)


def get_dict_1():
    return {
        "a": 1,
        "b": 2,
    }


def get_nested_dict_1():
    return {
        "a": 1,
        "b": {
            "g": 2,
        },
    }


def test_increment_dict_val():
    dic1 = get_dict_1()
    increment_dict_val(dic1, "a", 1)
    assert dic1["a"] == 2
    increment_dict_val(dic1, "c", 4)
    assert dic1["c"] == 4


def test_increment_nested_val():
    dic1 = get_nested_dict_1()
    increment_nested_val(dic1, ("a"), 1)
    assert dic1["a"] == 2
    increment_nested_val(dic1, ("c"), 3)
    assert dic1["c"] == 3
    increment_nested_val(dic1, ("b", "g"), 4)
    assert dic1["b"]["g"] == 6
    increment_nested_val(dic1, ("b", "z"), 17)
    assert dic1["b"]["z"] == 17


def test_get_first_val():
    dict_obj = {"a": 1, "c": 2}
    assert get_first_val(("a", "b", "c"), dict_obj) == 1
    assert get_first_val(("b", "c", "a"), dict_obj) == 2
    with pytest.raises(KeyError):
        get_first_val(("e",), dict_obj)


def test_any_in_dict():
    dict_obj = {"a": 1, "c": 2}
    assert any_in_dict(("a", "b"), dict_obj) is True
    assert any_in_dict(("b", "g"), dict_obj) is False


def test_get_nested_val():
    dict_obj = {"a": {"b": 7}}
    assert get_nested_val(("a", "b"), dict_obj) == 7
    with pytest.raises(KeyError):
        get_nested_val(("a", "c"), dict_obj)


def test_safe_nested_val():
    dict_obj = {"a": {"b": 7}}
    assert safe_nested_val(("a", "b"), dict_obj) == 7
    assert safe_nested_val(("a", "c"), dict_obj) is None
    assert safe_nested_val(("a", "c"), dict_obj, 5) == 5
    assert safe_nested_val(("d",), dict_obj, 5) == 5


def test_put_nested_val():
    dict_obj = {"a": {"h": 3}}
    put_nested_val(dict_obj, ("a", "b"), 7)
    assert dict_obj["a"]["b"] == 7
    put_nested_val(dict_obj, ("a", "b"), 12)
    assert dict_obj["a"]["b"] == 12
    put_nested_val(dict_obj, ("a", "g", "z"), 14)
    assert dict_obj["a"]["g"]["z"] == 14
    put_nested_val(dict_obj, ["base"], 88)
    assert dict_obj["base"] == 88


def test_in_nested_dicts():
    dict_obj = {"a": {"b": 7}}
    assert in_nested_dicts(("a", "b"), dict_obj) is True
    assert in_nested_dicts(("a", "c"), dict_obj) is False


def test_get_alternative_nested_val():
    dict_obj = {"a": {"b": 7}}
    assert get_alternative_nested_val(("a", ("b", "c")), dict_obj) == 7
    with pytest.raises(KeyError):
        get_alternative_nested_val(("a", ("x", "y")), dict_obj)


def test_safe_alternative_nested_val():
    dict_obj = {"a": {"b": 7}}
    assert safe_alternative_nested_val(("a", ("b", "c")), dict_obj) == 7
    assert safe_alternative_nested_val(("a", ("g", "c")), dict_obj) is None


def test_any_path_in_dict():
    dict_obj = {"a": {"b": 7}}
    assert any_path_in_dict(("a", ("b", "c")), dict_obj) is True
    assert any_path_in_dict(("a", ("x", "y")), dict_obj) is False


def test_subdict_by_keys():
    dict_obj = {"a": 1, "b": 2, "c": 3, "d": 4}
    subdict = subdict_by_keys(dict_obj, ["b", "d", "e"])
    assert subdict == {"b": 2, "d": 4}


def test_add_to_dict_val_set():
    dict_obj = {"a": {1, 2}}
    add_to_dict_val_set(dict_obj, "a", 2)
    assert dict_obj["a"] == {1, 2}
    add_to_dict_val_set(dict_obj, "a", 3)
    assert dict_obj["a"] == {1, 2, 3}
    add_to_dict_val_set(dict_obj, "b", 5)
    assert dict_obj["b"] == {5}


def test_add_many_to_dict_val_set():
    dict_obj = {"a": {1, 2}}
    add_many_to_dict_val_set(dict_obj, "a", [2, 3])
    assert dict_obj["a"] == {1, 2, 3}
    add_many_to_dict_val_set(dict_obj, "b", [2, 3])
    assert dict_obj["b"] == {2, 3}


def test_append_to_dict_val_list():
    dict_obj = {"a": [1, 2]}
    append_to_dict_val_list(dict_obj, "a", 3)
    assert dict_obj["a"] == [1, 2, 3]
    append_to_dict_val_list(dict_obj, "b", 5)
    assert dict_obj["b"] == [5]


def test_add_many_to_dict_val_list():
    dict_obj = {"a": [1, 2]}
    add_many_to_dict_val_list(dict_obj, "a", [2, 3])
    assert dict_obj["a"] == [1, 2, 2, 3]
    add_many_to_dict_val_list(dict_obj, "b", [2, 3])
    assert dict_obj["b"] == [2, 3]


def test_get_key_of_max():
    assert get_key_of_max({"a": 2, "b": 1}) == "a"


def test_get_keys_of_max_n():
    dict_obj = {"a": 2, "b": 1, "c": 5}
    assert get_keys_of_max_n(dict_obj, 2) == ["a", "c"]


def test_get_key_of_min():
    assert get_key_of_min({"a": 2, "b": 1}) == "b"


def test_get_key_val_of_max():
    assert get_key_val_of_max({"a": 2, "b": 1}) == ("a", 2)


def test_get_key_val_of_max_key():
    assert get_key_val_of_max_key({5: "g", 3: "z"}) == (5, "g")


def test_unite_dicts():
    dict_obj = {"a": 2, "b": 1}
    dict_obj2 = {"a": 8, "c": 5}
    united = unite_dicts(dict_obj, dict_obj2)
    assert united == {"a": 8, "b": 1, "c": 5}


def test_deep_merge_dict():
    base = {"a": 1, "b": 2, "c": {"d": 4}, "e": 5}
    priority = {"a": {"g": 7}, "c": 3, "e": 5, "f": 6}
    result = deep_merge_dict(base, priority)
    assert result == {"a": {"g": 7}, "b": 2, "c": 3, "e": 5, "f": 6}


def test_norm_int_dict():
    dict_obj = {"a": 3, "b": 5, "c": 2}
    result = norm_int_dict(dict_obj)
    assert result == {"a": 0.3, "b": 0.5, "c": 0.2}


def test_sum_num_dicts():
    dict1 = {"a": 3, "b": 2}
    dict2 = {"a": 7, "c": 8}
    assert sum_num_dicts([dict1, dict2]) == {"a": 10, "b": 2, "c": 8}
    result = sum_num_dicts([dict1, dict2], normalize=True)
    assert result == {"a": 0.5, "b": 0.1, "c": 0.4}


def test_sum_dicts():
    dict1 = {"a": 3, "b": "hello"}
    dict2 = {"a": 7, "b": "world", "c": 8}
    result = sum_dicts([dict1, dict2])
    assert result["a"] == 10
    assert result["b"] == "world"
    assert result["c"] == 8


def test_reverse_dict():
    dicti = {"a": 1, "b": 3, "c": 1}
    assert reverse_dict(dicti) == {1: ["a", "c"], 3: ["b"]}


def test_reverse_dict_partial():
    dicti = {"a": 1, "b": 3}
    assert reverse_dict_partial(dicti) == {1: "a", 3: "b"}


def test_reverse_list_valued_dict():
    dicti = {"a": [1, 2], "b": [3, 4]}
    assert reverse_list_valued_dict(dicti) == {1: "a", 2: "a", 3: "b", 4: "b"}


def test_flatten_dict():
    dicti = {"a": 1, "b": {"g": 4, "o": 9}, "x": [4, "d"]}
    result = flatten_dict(dicti)
    assert result == {"a": 1, "b.g": 4, "b.o": 9, "x.0": 4, "x.1": "d"}


def test_key_value_nested_generator():
    dicti = {"a": 1, "b": {"c": 3, "d": 4}}
    assert sorted(key_value_nested_generator(dicti)) == [
        ("a", 1),
        ("c", 3),
        ("d", 4),
    ]


def test_key_tuple_value_nested_generator():
    dicti = {"a": 1, "b": {"c": 3, "d": 4}}
    assert sorted(key_tuple_value_nested_generator(dicti)) == [
        (("a",), 1),
        (("b", "c"), 3),
        (("b", "d"), 4),
    ]


def test_sum_dicts_normalize():
    dict1 = {"a": 3, "b": 2}
    dict2 = {"a": 7, "c": 8}
    result = sum_dicts([dict1, dict2], normalize=True)
    assert result["a"] == pytest.approx(0.5)
    assert result["b"] == pytest.approx(0.1)
    assert result["c"] == pytest.approx(0.4)


def test_pprint_int_dict(capsys):
    pprint_int_dict({"a": 3, "b": 1})
    captured = capsys.readouterr()
    assert "a" in captured.out
    assert "3" in captured.out
    pprint_int_dict({"a": 3, "b": 1}, descending=True)
    captured = capsys.readouterr()
    assert "a" in captured.out


def test_pprint_dist_dict(capsys):
    pprint_dist_dict({"a": 0.7, "b": 0.3})
    captured = capsys.readouterr()
    assert "a" in captured.out
    assert "70.00" in captured.out
    pprint_dist_dict({"a": 0.7, "b": 0.3}, descending=True)
    captured = capsys.readouterr()
    assert "a" in captured.out

