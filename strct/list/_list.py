"""list-related utility functions."""


def hash_list(list_obj):
    """Computes a hash value for the given list.

    The list must contain only hashable keys and values.

    Arguments
    ---------
    list_obj : list
        The list for which to compute a hash value.

    Returns
    -------
    int
        The computed hash value.
    """
    return hash(frozenset(list_obj))


def order_preserving_single_index_shift(arr, index, new_index):
    """Moves a list element to a new index while preserving order.

    Arguments
    ---------
    arr : list
        The list in which to shift an element.
    index : int
        The index of the element to shift.
    new_index : int
        The index to which to shift the element.

    Returns
    -------
    list
        The list with the element shifted.

    Example
    -------
    >>> arr = ['a', 'b', 'c', 'd']
    >>> order_preserving_single_index_shift(arr, 2, 0)
    ['c', 'a', 'b', 'd']
    >>> order_preserving_single_index_shift(arr, 2, 3)
    ['a', 'b', 'd', 'c']
    """
    if new_index == 0:
        return [arr[index]] + arr[0:index] + arr[index+1:]
    if new_index == len(arr) - 1:
        return arr[0:index] + arr[index+1:] + [arr[index]]
    if index < new_index:
        return arr[0:index] + arr[index+1:new_index+1] + [arr[index]] + arr[
            new_index+1:]
    if new_index <= index:
        return arr[0:new_index] + [arr[index]] + arr[new_index:index] + arr[
            index+1:]


def order_preserving_single_element_shift(arr, value, new_index):
    """Moves a list element to a new index while preserving order.

    Arguments
    ---------
    arr : list
        The list in which to shift an element.
    value : object
        The value of the element to shift.
    new_index : int
        The index to which to shift the element.

    Returns
    -------
    list
        The list with the element shifted.

    Example
    -------
    >>> arr = ['a', 'b', 'c', 'd']
    >>> order_preserving_single_element_shift(['a', 'b', 'c', 'd'], 'c', 0)
    ['c', 'a', 'b', 'd']
    """
    return order_preserving_single_index_shift(
        arr=arr, index=arr.index(value), new_index=new_index)
