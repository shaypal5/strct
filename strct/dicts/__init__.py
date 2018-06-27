"""dict-related utility functions."""

from ._dict import (  # noqa: F401
    # functions
    get_nested_val,
    safe_nested_val,
    put_nested_val,
    in_nested_dicts,
    get_alternative_nested_val,
    safe_alternative_nested_val,
    any_path_in_dict,
    subdict_by_keys,
    increment_dict_val,
    increment_nested_val,
    add_to_dict_val_set,
    add_many_to_dict_val_set,
    add_many_to_dict_val_list,
    get_key_of_max,
    get_keys_of_max_n,
    get_key_of_min,
    get_key_val_of_max,
    get_key_val_of_max_key,
    unite_dicts,
    deep_merge_dict,
    norm_int_dict,
    sum_num_dicts,
    sum_dicts,
    reverse_dict,
    reverse_dict_partial,
    reverse_list_valued_dict,
    flatten_dict,
    pprint_int_dict,
    pprint_dist_dict,
    key_value_nested_generator,
    key_tuple_value_nested_generator,
    # classes
    CaseInsensitiveDict,
)
try:
    del _dict  # noqa: F821
except NameError:
    pass
