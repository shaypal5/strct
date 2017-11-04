"""General data-structure related utility functions."""

import json
import hashlib

from strct.dicts import hash_dict
from strct.lists import hash_list


def stable_hash_builtins_strct(strct_obj):
    """Computes a cross-kernel stable hash value for the given data structure.

    The supported data structure are the built-in list, tuple and dict types.
    If the given strct is a tuple or a list, it

    Any included list, whether outer or nested, may only contain values of the
    following built-in types: bool, int, float, complex, str, list, tuple, dict.

    Any included dict, whether outer or nested, may only contain keys of a
    single type, which can be one the following built-in types: bool, int,
    float, str, and may only contain values of only the following built-in
    types: bool, int, float, complex, str, list, tuple, dict.

    Arguments
    ---------
    strct_obj : dict/list/tuple
        The data structure for which to compute a hash value.

    Returns
    -------
    int
        The computed hash value.
    """
    encoded_str = json.dumps(
        obj=strct_obj,
        skipkeys=False,
        ensure_ascii=False,
        check_circular=True,
        allow_nan=True,
        cls=None,
        indent=0,
        separators=(',', ':'),
        default=None,
        sort_keys=True,
    ).encode('utf-8')
    return hashlib.sha256(encoded_str).hexdigest()


def hash_dict_list(dict_list):
    """Computes a hash value for the given list of dicts.

    Each dict in the list must contain only hashable keys and values.

    Arguments
    ---------
    dict_list : list
        The list of dicts for which to compute a hash value.

    Returns
    -------
    int
        The computed hash value.
    """
    return hash_list([hash_dict(dic) for dic in dict_list])
