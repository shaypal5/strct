"""list-related utility functions."""


def all_but(list_obj, idx):
    """Returns the given list will all but a single item.

    Parameters
    ----------
    list_obj : list
        The list from which to take out an element.
    idx : int
        The index of the element to take out.

    Returns
    -------
    list
        The list with the element taken out.

    Example
    -------
    >>> arr = [12, 34, 5, 54]
    >>> all_but(arr, 2)
    [12, 34, 54]
    >>> all_but(arr, 0)
    [34, 5, 54]
    >>> all_but(arr, 3)
    [12, 34, 5]
    """
    return list_obj[0:idx] + list_obj[idx+1:]


def order_preserving_single_index_shift(arr, index, new_index):
    """Moves a list element to a new index while preserving order.

    Parameters
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

    Parameters
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
