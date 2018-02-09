"""dict-related utility functions."""

import copy  # for deep copies of dicts
import numbers


def get_first_val(key_tuple, dict_obj):
    """Return the first value mapped by a key in the given tuple.

    Parameters
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

    Parameters
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

    Parameters
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

    Parameters
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


def put_nested_val(dict_obj, key_tuple, value):
    """Put a value into nested dicts by the order of the given keys tuple.

    Any missing intermediate dicts are created.

    Parameters
    ---------
    dict_obj : dict
        The outer-most dict to put in.
    key_tuple : tuple
        The keys to use for putting, in order.
    value : object
        The value to put.

    Example:
    --------
    >>> dict_obj = {'a': {'h': 3}}
    >>> put_nested_val(dict_obj, ('a', 'b'), 7)
    >>> dict_obj['a']['b']
    7
    >>> put_nested_val(dict_obj, ('a', 'b'), 12)
    >>> dict_obj['a']['b']
    12
    >>> put_nested_val(dict_obj, ('a', 'g', 'z'), 14)
    >>> dict_obj['a']['g']['z']
    14
    >>> put_nested_val(dict_obj, ['base'], 88)
    >>> dict_obj['base']
    88
    """
    current_dict = dict_obj
    for key in key_tuple[:-1]:
        try:
            current_dict = current_dict[key]
        except KeyError:
            current_dict[key] = {}
            current_dict = current_dict[key]
    current_dict[key_tuple[-1]] = value


def in_nested_dicts(key_tuple, dict_obj):
    """Indicated whether a value is nested in nested dicts by a keys tuple.

    Parameters
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

    Parameters
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

    Parameters
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

    Parameters
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

    Example
    -------
    >>> dict_obj = {'a': set([1, 2])}
    >>> add_to_dict_val_set(dict_obj, 'a', 2)
    >>> print(dict_obj['a'])
    {1, 2}
    >>> add_to_dict_val_set(dict_obj, 'a', 3)
    >>> print(dict_obj['a'])
    {1, 2, 3}
    """
    try:
        dict_obj[key].add(val)
    except KeyError:
        dict_obj[key] = set([val])


def add_many_to_dict_val_set(dict_obj, key, val_list):
    """Adds the given value list to the set mapped by the given key.
    If the key is missing from the dict, the given mapping is added.

    Example
    -------
    >>> dict_obj = {'a': set([1, 2])}
    >>> add_many_to_dict_val_set(dict_obj, 'a', [2, 3])
    >>> print(dict_obj['a'])
    {1, 2, 3}
    >>> add_many_to_dict_val_set(dict_obj, 'b', [2, 3])
    >>> print(dict_obj['b'])
    {2, 3}
    """
    try:
        dict_obj[key].update(val_list)
    except KeyError:
        dict_obj[key] = set(val_list)


def add_many_to_dict_val_list(dict_obj, key, val_list):
    """Adds the given value list to the list mapped by the given key.
    If the key is missing from the dict, the given mapping is added.

    Example
    -------
    >>> dict_obj = {'a': [1, 2]}
    >>> add_many_to_dict_val_list(dict_obj, 'a', [2, 3])
    >>> print(dict_obj['a'])
    [1, 2, 2, 3]
    >>> add_many_to_dict_val_list(dict_obj, 'b', [2, 3])
    >>> print(dict_obj['b'])
    [2, 3]
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


def unite_dicts(*args):
    """Unites the given dicts into a single dict mapping each key to the
    latest value it was mapped to in the order the dicts were given.

    Parameters
    ---------
    *args : positional arguments, each of type dict
        The dicts to unite.

    Returns
    -------
    dict
        A dict where each key is mapped to the latest value it was mapped to
        in the order the dicts were given

    Example:
    --------
    >>> dict_obj = {'a':2, 'b':1}
    >>> dict_obj2 = {'a':8, 'c':5}
    >>> united = unite_dicts(dict_obj, dict_obj2)
    >>> print(sorted(united.items()))
    [('a', 8), ('b', 1), ('c', 5)]
    """
    return dict(i for dct in args for i in dct.items())


def deep_merge_dict(base, priority):
    """Recursively merges the two given dicts into a single dict.

    Treating base as the the initial point of the resulting merged dict,
    and considering the nested dictionaries as trees, they are merged os:
    1. Every path to every leaf in priority would be represented in the result.
    2. Subtrees of base are overwritten if a leaf is found in the
    corresponding path in priority.
    3. The invariant that all priority leaf nodes remain leafs is maintained.


    Parameters
    ----------
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

    Parameters
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

    Parameters
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

    Parameters
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

    Parameters
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

    Parameters
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

    Parameters
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


def _get_key_reducer(separator):
    def _key_reducer(key1, key2):
        if key1 is None:
            return key2
        return key1 + separator + key2
    return _key_reducer


def flatten_dict(dict_obj, separator='.', flatten_lists=False):
    """Flattens the given dict into a single-level dict with flattend keys.

    Parameters
    ---------
    dict_obj : dict
        A possibly nested dict.
    separator : str, optional
        The character to use as a separator between keys. Defaults to '.'.
    flatten_lists : bool, optional
        If True, list values are also flattened. False by default.

    Returns
    -------
    dict
        A shallow dict, where no value is a dict in itself, and keys are
        concatenations of original key paths separated with the given
        separator.

    Example
    -------
    >>> dicti = {'a': 1, 'b': {'g': 4, 'o': 9}, 'x': [4, 'd']}
    >>> flat = flatten_dict(dicti)
    >>> sorted(flat.items())
    [('a', 1), ('b.g', 4), ('b.o', 9), ('x.0', 4), ('x.1', 'd')]
    """
    reducer = _get_key_reducer(separator)
    flat = {}

    def _flatten_key_val(key, val, parent):
        flat_key = reducer(parent, key)
        try:
            _flatten(val, flat_key)
        except TypeError:
            flat[flat_key] = val

    def _flatten(d, parent=None):
        try:
            for key, val in d.items():
                _flatten_key_val(key, val, parent)
        except AttributeError:
            if isinstance(d, (str, bytes)):
                raise TypeError
            for i, value in enumerate(d):
                _flatten_key_val(str(i), value, parent)
    _flatten(dict_obj)
    return flat


def pprint_int_dict(int_dict, indent=4, descending=False):
    """Prints the given dict with int values in a nice way.

    Parameters
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

    Parameters
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


def key_value_nested_generator(dict_obj):
    """Recursively iterate over key-value pairs of nested dictionaries.

    Parameters
    ---------
    dict_obj : dict
        The outer-most dict to iterate on.

    Returns
    -------
    generator
        A generator over key-value pairs in all nested dictionaries.

    Example
    -------
    >>> dicti = {'a': 1, 'b': {'c': 3, 'd': 4}}
    >>> print(sorted(list(key_value_nested_generator(dicti))))
    [('a', 1), ('c', 3), ('d', 4)]
    """
    for key, value in dict_obj.items():
        if isinstance(value, dict):
            for key, value in key_value_nested_generator(value):
                yield key, value
        else:
            yield key, value


def key_tuple_value_nested_generator(dict_obj):
    """Recursively iterate over key-tuple-value pairs of nested dictionaries.

    Parameters
    ---------
    dict_obj : dict
        The outer-most dict to iterate on.

    Returns
    -------
    generator
        A generator over key-tuple-value pairs in all nested dictionaries.

    Example
    -------
    >>> dicti = {'a': 1, 'b': {'c': 3, 'd': 4}}
    >>> print(sorted(list(key_tuple_value_nested_generator(dicti))))
    [(('a',), 1), (('b', 'c'), 3), (('b', 'd'), 4)]
    """
    for key, value in dict_obj.items():
        if isinstance(value, dict):
            for nested_key, value in key_tuple_value_nested_generator(value):
                yield tuple([key]) + nested_key, value
        else:
            yield tuple([key]), value
