"""Data structure hashing related utility functions."""

import json
import hashlib


def _stable_hash_primitive(primitive):
    try:  # assume it's a string...
        return int.from_bytes(
            hashlib.sha256(primitive.encode('UTF-8')).digest(),
            byteorder='little',
        )
    except AttributeError:  # if not, assume it's an int or float
        try:
            return int(primitive)
        except TypeError:  # if not, assume it's a complex number
            try:
                return int(primitive.real)
            except AttributeError:
                raise TypeError(
                    "Object {} of unhashable type encountered!".format(
                        primitive))


def _recursive_stable_hash(obj):
    try:  # assume it's a dict
        item_hashes = []
        for item in obj.items():
            try:
                item_hashes.append(_recursive_stable_hash(item))
            except TypeError:
                raise TypeError("dict includes unhashable values.")
        return hash(frozenset(item_hashes))
    except AttributeError:
        pass  # go on to assume it's an iterable
    try:  # assume it's an iterable
        if not isinstance(obj, (str, bytes)):
            return hash(frozenset([_recursive_stable_hash(i) for i in obj]))
        else:
            return _stable_hash_primitive(obj)
    except TypeError:
        pass  # go on to assume it's a primitive
    return _stable_hash_primitive(obj)


def stable_hash(obj):
    """Computes a cross-kernel stable hash value for the given object.

    The supported data structure are the built-in list, tuple and dict types.

    Any included tuple or list, whether outer or nested, may only contain
    values of the following built-in types: bool, int, float, complex, str,
    list, tuple and dict.

    Any included dict, whether outer or nested, may only contain keys of a
    single type, which can be one the following built-in types: bool, int,
    float, str, and may only contain values of only the following built-in
    types: bool, int, float, complex, str, list, tuple, dict.

    Parameters
    ---------
    obj : bool/int/float/complex/str/dict/list/tuple
        The object for which to compute a hash value.

    Returns
    -------
    int
        The computed hash value.

    Example
    -------
    >>> stable_hash(2.2)
    2
    >>> stable_hash(complex(4, 5))
    4
    >>> stable_hash([3, 23.2, '23'])
    -8814990287216496045
    >>> stable_hash([34, {'a': 23, 'g': [1, '43']}])
    4894511948741237771
    >>> stable_hash({'a': 23, 'b': [234, 'g'], 'c': {4: 'go'}})
    -4531592806763782902
    """
    return _recursive_stable_hash(obj)


def json_based_stable_hash(obj):
    """Computes a cross-kernel stable hash value for the given object.

    The supported data structure are the built-in list, tuple and dict types.

    Any included tuple or list, whether outer or nested, may only contain
    values of the following built-in types: bool, int, float, complex, str,
    list, tuple and dict.

    Any included dict, whether outer or nested, may only contain keys of a
    single type, which can be one the following built-in types: bool, int,
    float, str, and may only contain values of only the following built-in
    types: bool, int, float, complex, str, list, tuple, dict.

    Parameters
    ---------
    obj : bool/int/float/complex/str/dict/list/tuple
        The object for which to compute a hash value.

    Returns
    -------
    int
        The computed hash value.
    """
    encoded_str = json.dumps(
        obj=obj,
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
