"""Dict-related utility functions."""

from ._dict import (  # noqa: F401
    # classes
    CaseInsensitiveDict,
    add_many_to_dict_val_list,
    add_many_to_dict_val_set,
    add_to_dict_val_set,
    any_path_in_dict,
    append_to_dict_val_list,
    deep_merge_dict,
    flatten_dict,
    get_alternative_nested_val,
    get_key_of_max,
    get_key_of_min,
    get_key_val_of_max,
    get_key_val_of_max_key,
    get_keys_of_max_n,
    # functions
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

from contextlib import suppress
with suppress(NameError):
    del _dict
