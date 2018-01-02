"""dict-related utility functions."""

from ._dict import (
    get_nested_val,
    safe_nested_val,
    in_nested_dicts,
    get_alternative_nested_val,
    safe_alternative_nested_val,
    any_path_in_dict,
    increment_dict_val,
    add_to_dict_val_set,
    add_many_to_dict_val_set,
    add_many_to_dict_val_list,
    get_key_of_max,
    get_keys_of_max_n,
    get_key_of_min,
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
)
try:
    del _dict
except NameError:
    pass
