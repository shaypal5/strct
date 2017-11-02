"""dict-related utility functions."""

import copy  # for deep copies of dicts
import json
import numbers
import hashlib


def hash_dict(dict_obj):
    """Recursively computes a hash value for the given dict.

    The dict must contain only hashable keys and values. This hash value is not
    stable across different python kernels.

    Arguments
    ---------
    dict_obj : dict
        The dict for which to compute a hash value.

    Returns
    -------
    int
        The computed hash value.
    """
    item_hashes = []
    for item in dict_obj.items():
        try:
            item_hashes.append(hash(item))
        except TypeError:
            try:
                dummy_item = (item[0], hash_dict(item[1]))
                item_hashes.append(hash(dummy_item))
            except AttributeError:
                raise ValueError("dict includes unhashable values.")
    return hash(frozenset(item_hashes))


def get_first_val(key_tuple, dict_obj):
    """Return the first value mapped by a key in the given tuple.

    Arguments
    ---------
    key_tuple : tuple
        The keys to use for extraction, in order.
    dict_obj : dict
        The dict to extract from.

    Returns
    -------
    value : object
        The extracted value, if exists. Otherwise, raises KeyError.

    Example:
    --------
    >>> dict_obj = {'a': 1, 'c': 2}
    >>> get_first_val(('a', 'b', 'c'), dict_obj)
    1
    >>> get_first_val(('b', 'c', 'a'), dict_obj)
    2
    >>> get_first_val(('e'), dict_obj)
    Traceback (most recent call last):
     ...
    KeyError: 'None of the provided keys was found'
    """
    for key in key_tuple:
        try:
            return dict_obj[key]
        except KeyError:
            pass
    raise KeyError('None of the provided keys was found')


def any_in_dict(key_tuple, dict_obj):
    """Return whether any of the given keys is in the given dict.

    Arguments
    ---------
    key_tuple : tuple
        The keys for which to check inclusion.
    dict_obj : dict
        The dict to examine.

    Returns
    -------
    bool
        True if any of the given keys is in the given dict. False otherwise.

    Example:
    --------
    >>> dict_obj = {'a': 1, 'c': 2}
    >>> any_in_dict(('a', 'b'), dict_obj)
    True
    >>> any_in_dict(('b', 'g'), dict_obj)
    False
    """
    return any([key in dict_obj for key in key_tuple])


def get_nested_val(key_tuple, dict_obj):
    """Return a value from nested dicts by the order of the given keys tuple.

    Arguments
    ---------
    key_tuple : tuple
        The keys to use for extraction, in order.
    dict_obj : dict
        The outer-most dict to extract from.

    Returns
    -------
    value : object
        The extracted value, if exists. Otherwise, raises KeyError.

    Example:
    --------
    >>> dict_obj = {'a': {'b': 7}}
    >>> get_nested_val(('a', 'b'), dict_obj)
    7
    """
    if len(key_tuple) == 1:
        return dict_obj[key_tuple[0]]
    return get_nested_val(key_tuple[1:], dict_obj[key_tuple[0]])


def safe_nested_val(key_tuple, dict_obj, default_value=None):
    """Return a value from nested dicts by the order of the given keys tuple.

    Arguments
    ---------
    key_tuple : tuple
        The keys to use for extraction, in order.
    dict_obj : dict
        The outer-most dict to extract from.
    default_value : object, default None
        The value to return when no matching nested value is found.

    Returns
    -------
    value : object
        The extracted value, if exists. Otherwise, the given default_value.

    Example:
    --------
    >>> dict_obj = {'a': {'b': 7}}
    >>> safe_nested_val(('a', 'b'), dict_obj)
    7
    >>> safe_nested_val(('a', 'c'), dict_obj)

    >>> safe_nested_val(('a', 'c'), dict_obj, 5)
    5
    >>> safe_nested_val(('d'), dict_obj, 5)
    5
    """
    try:
        return get_nested_val(key_tuple, dict_obj)
    except (KeyError, IndexError, TypeError):
        return default_value


def in_nested_dicts(key_tuple, dict_obj):
    """Indicated whether a value is nested in nested dicts by a keys tuple.

    Arguments
    ---------
    key_tuple : tuple
        The keys to use for examination, in order.
    dict_obj : dict
        The outer-most dict to examine from.

    Returns
    -------
    True : object
        If some value if nested in the given dict by the given keys tupe, in
        order. False otherwise.

    Example:
    --------
    >>> dict_obj = {'a': {'b': 7}}
    >>> in_nested_dicts(('a', 'b'), dict_obj)
    True
    >>> in_nested_dicts(('a', 'c'), dict_obj)
    False
    """
    return safe_nested_val(key_tuple, dict_obj) is not None


def get_alternative_nested_val(key_tuple, dict_obj):
    """Return a value from nested dicts by any path in the given keys tuple.

    Arguments
    ---------
    key_tuple : tuple
        Describe all possible paths for extraction.
    dict_obj : dict
        The outer-most dict to extract from.

    Returns
    -------
    value : object
        The extracted value, if exists. Otherwise, raises KeyError.

    Example:
    --------
    >>> dict_obj = {'a': {'b': 7}}
    >>> get_alternative_nested_val(('a', ('b', 'c')), dict_obj)
    7
    """
    # print('key_tuple: {}'.format(key_tuple))
    # print('dict_obj: {}'.format(dict_obj))
    top_keys = key_tuple[0] if isinstance(key_tuple[0], (list, tuple)) else [
        key_tuple[0]]
    for key in top_keys:
        try:
            if len(key_tuple) < 2:
                return dict_obj[key]
            return get_alternative_nested_val(key_tuple[1:], dict_obj[key])
        except (KeyError, TypeError, IndexError):
            pass
    raise KeyError


def safe_alternative_nested_val(key_tuple, dict_obj, default_value=None):
    """Return a value from nested dicts by any path in the given keys tuple.

    Arguments
    ---------
    key_tuple : tuple
        Describe all possible paths for extraction.
    dict_obj : dict
        The outer-most dict to extract from.
    default_value : object, default None
        The value to return when no matching nested value is found.

    Returns
    -------
    value : object
        The extracted value, if exists. Otherwise, the given default_value.

    Example:
    --------
    >>> dict_obj = {'a': {'b': 7}}
    >>> safe_alternative_nested_val(('a', ('b', 'c')), dict_obj)
    7
    >>> safe_alternative_nested_val(('a', ('g', 'c')), dict_obj)

    """
    try:
        return get_alternative_nested_val(key_tuple, dict_obj)
    except KeyError:
        return default_value


def any_path_in_dict(key_tuple, dict_obj):
    """Indicated whether any path in the given keys tuple is in a dict.

    Arguments
    ---------
    key_tuple : tuple
        Describe all possible paths for examination.
    dict_obj : dict
        The outer-most dict to examine from.

    Returns
    -------
    bool
        True if any path in the given keys tuple is in the given dict. False
        otherwise.

    Example:
    --------
    >>> dict_obj = {'a': {'b': 7}}
    >>> any_path_in_dict(('a', ('b', 'c')), dict_obj)
    True
    """
    return safe_alternative_nested_val(key_tuple, dict_obj) is not None


def increment_dict_val(dict_obj, key, val):
    """Increments the value mapped by the given key by the given val.
    If the key is missing from the dict, the given mapping is added.

    Example:
    --------
    >>> dict_obj = {'a':2, 'b':1}
    >>> increment_dict_val(dict_obj, 'a', 4)
    >>> print(dict_obj['a'])
    6
    >>> increment_dict_val(dict_obj, 'd', 4)
    >>> print(dict_obj['d'])
    4
    """
    dict_obj[key] = dict_obj.get(key, 0) + val


def add_to_dict_val_set(dict_obj, key, val):
    """Adds the given val to the set mapped by the given key.
    If the key is missing from the dict, the given mapping is added.
    """
    try:
        dict_obj[key].add(val)
    except KeyError:
        dict_obj[key] = set([val])


def add_many_to_dict_val_set(dict_obj, key, val_list):
    """Adds the given value list to the set mapped by the given key.
    If the key is missing from the dict, the given mapping is added.
    """
    print(key)
    try:
        dict_obj[key].update(val_list)
    except KeyError:
        dict_obj[key] = set(val_list)


def add_many_to_dict_val_list(dict_obj, key, val_list):
    """Adds the given value list to the list mapped by the given key.
    If the key is missing from the dict, the given mapping is added.
    """
    try:
        dict_obj[key].extend(val_list)
    except KeyError:
        dict_obj[key] = list(val_list)


def get_key_of_max(dict_obj):
    """Returns the key that maps to the maximal value in the given dict.

    Example:
    --------
    >>> dict_obj = {'a':2, 'b':1}
    >>> print(get_key_of_max(dict_obj))
    a
    """
    return max(
        dict_obj, key=lambda key: dict_obj[key])


def get_keys_of_max_n(dict_obj, n):
    """Returns the keys that maps to the top n max values in the given dict.

    Example:
    --------
    >>> dict_obj = {'a':2, 'b':1, 'c':5}
    >>> get_keys_of_max_n(dict_obj, 2)
    ['a', 'c']
    """
    return sorted([
        item[0]
        for item in sorted(
            dict_obj.items(), key=lambda item: item[1], reverse=True
        )[:n]
    ])


def get_key_of_min(dict_obj):
    """Returns the key that maps to the minimal value in the given dict.

    Example:
    --------
    >>> dict_obj = {'a':2, 'b':1}
    >>> print(get_key_of_min(dict_obj))
    b
    """
    return min(
        dict_obj, key=lambda key: dict_obj[key])


def unite_dicts(dicts):
    """Unites the given dicts into a single dict mapping each key to the
    latest value it was mapped to in the order the dicts were given.

    Arguments
    ---------
    dicts : list
        A list of dict objects.

    Returns
    -------
    dict
        A dict where each key is mapped to the latest value it was mapped to
        in the order the dicts were given
    """
    return dict(i for dct in dicts for i in dct.items())


def deep_merge_dict(base, priority):
    """Recursively merges the two given dicts into a single dict.abs

    Treating base as the the initial point of the resulting merged dict,
    and considering the nested dictionaries as trees, they are merged os:
    1. Every path to every leaf in priority would be represented in the result.
    2. Subtrees of base are overwritten if a leaf is found in the
    corresponding path in priority.
    3. The invariant that all priority leaf nodes remain leafs is maintained.


    Arguments
    ---------
    base : dict
        The first, lower-priority, dict to merge.
    priority : dict
        The second, higher-priority, dict to merge.
    Returns
    -------
    dict
        A recursive merge of the two given dicts.
    """
    if not isinstance(base, dict) or not isinstance(priority, dict):
        return priority
    result = copy.deepcopy(base)
    for key in priority.keys():
        if key in base:
            result[key] = deep_merge_dict(base[key], priority[key])
        else:
            result[key] = priority[key]
    return result


def norm_int_dict(int_dict):
    """Normalizes values in the given dict with int values.

    Arguments
    ---------
    int_dict : list
        A dict object mapping each key to an int value.

    Returns
    -------
    dict
        A dict where each key is mapped to its relative part in the sum of
        all dict values.
    """
    norm_dict = int_dict.copy()
    val_sum = sum(norm_dict.values())
    for key in norm_dict:
        norm_dict[key] = norm_dict[key] / val_sum
    return norm_dict


def sum_num_dicts(dicts, normalize=False):
    """Sums the given dicts into a single dict mapping each key to the sum
    of its mappings in all given dicts.

    Arguments
    ---------
    dicts : list
        A list of dict objects mapping each key to an numeric value.
    normalize : bool, default False
        Indicated whether to normalize all values by value sum.

    Returns
    -------
    dict
        A dict where each key is mapped to the sum of its mappings in all
        given dicts.
    """
    sum_dict = {}
    for dicti in dicts:
        for key in dicti:
            sum_dict[key] = sum_dict.get(key, 0) + dicti[key]
    if normalize:
        return norm_int_dict(sum_dict)
    return sum_dict


def sum_dicts(dicts, normalize=False):
    """Sums the given dicts into a single dict mapping each numberic-valued
    key to the sum of its mappings in all given dicts. Keys mapping to
    non-numeric values retain the last value (by the given order).

    Arguments
    ---------
    dicts : list
        A list of dict objects mapping each key to an numeric value.
    normalize : bool, default False
        Indicated whether to normalize all values by value sum.

    Returns
    -------
    dict
        A dict where each key is mapped to the sum of its mappings in all
        given dicts.
    """
    sum_dict = {}
    for dicti in dicts:
        for key in dicti:
            val = dicti[key]
            if isinstance(val, numbers.Number):
                sum_dict[key] = sum_dict.get(key, 0) + val
            else:
                sum_dict[key] = val
    if normalize:
        return norm_int_dict(sum_dict)
    return sum_dict


def reverse_dict(dict_obj):
    """Reverse a dict, so each value in it maps to a sorted list of its keys.

    Arguments
    ---------
    dict_obj : dict
        A key-value dict.

    Returns
    -------
    dict
        A dict where each value maps to a sorted list of all the unique keys
        that mapped to it.

    Example
    -------
    >>> dicti = {'a': 1, 'b': 3, 'c': 1}
    >>> reverse_dict(dicti)
    {1: ['a', 'c'], 3: ['b']}
    """
    new_dict = {}
    for key in dict_obj:
        add_to_dict_val_set(dict_obj=new_dict, key=dict_obj[key], val=key)
    for key in new_dict:
        new_dict[key] = sorted(new_dict[key], reverse=False)
    return new_dict


def reverse_dict_partial(dict_obj):
    """Reverse a dict, so each value in it maps to one of its keys.

    Arguments
    ---------
    dict_obj : dict
        A key-value dict.

    Returns
    -------
    dict
        A dict where each value maps to the key that mapped to it.

    Example
    -------
    >>> dicti = {'a': 1, 'b': 3}
    >>> reverse_dict_partial(dicti)
    {1: 'a', 3: 'b'}
    """
    new_dict = {}
    for key in dict_obj:
        new_dict[dict_obj[key]] = key
    return new_dict


def reverse_list_valued_dict(dict_obj):
    """Reverse a list-valued dict, so each element in a list maps to its key.

    Arguments
    ---------
    dict_obj : dict
        A dict where each key maps to a list of unique values. Values are
        assumed to be unique across the entire dict, on not just per-list.

    Returns
    -------
    dict
        A dict where each element in a value list of the input dict maps to
        the key that mapped to the list it belongs to.

    Example
    -------
    >>> dicti = {'a': [1, 2], 'b': [3, 4]}
    >>> reverse_list_valued_dict(dicti)
    {1: 'a', 2: 'a', 3: 'b', 4: 'b'}
    """
    new_dict = {}
    for key in dict_obj:
        for element in dict_obj[key]:
            new_dict[element] = key
    return new_dict


def pprint_int_dict(int_dict, indent=4, descending=False):
    """Prints the given dict with int values in a nice way.

    Arguments
    ---------
    int_dict : list
        A dict object mapping each key to an int value.
    """
    sorted_tup = sorted(int_dict.items(), key=lambda x: x[1])
    if descending:
        sorted_tup.reverse()
    print('{')
    for tup in sorted_tup:
        print('{}{}: {}'.format(' '*indent, tup[0], tup[1]))
    print('}')


def pprint_dist_dict(int_dict, indent=4, descending=False):
    """Prints the given dict, representing a normalized distribution, nicely.

    Arguments
    ---------
    int_dict : list
        A dict object mapping each key to an int value between 0 and 1, and all
        values sum to 1.
    """
    sorted_tup = sorted(int_dict.items(), key=lambda x: x[1])
    if descending:
        sorted_tup.reverse()
    print('{')
    for tup in sorted_tup:
        print('{}{}: {:.2f} %'.format(' '*indent, tup[0], tup[1]*100))
    print('}')
