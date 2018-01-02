"""dict-related utility functions."""


def get_priority_elem_in_set(obj_set, priority_list):
    """Returns the highest priority element in a set.

    The set will be searched for objects in the order they appear in the
    priority list, and the first one to be found will be returned. None is
    returned if no such object is found.

    Parameters
    ---------
    obj_set : set, list
        A set or list of objects.
    priority_list : list
        A list of objects in descending order of priority.

    Returns
    -------
    object
        The highest priority object in the given set.

    Example:
    --------
    >>> obj_set = set([3, 2, 7, 8])
    >>> priority_list = [4, 8, 1, 3]
    >>> print(get_priority_elem_in_set(obj_set, priority_list))
    8
    """
    for obj in priority_list:
        if obj in obj_set:
            return obj
    return None
