"""sortedlist-related utility functions."""


def find_point_in_section_list(point, section_list):
    """Returns the start of the section the given point belongs to.

    The given list is assumed to contain start points of consecutive
    sections, except for the final point, assumed to be the end point of the
    last section. For example, the list [5, 8, 30, 31] is interpreted as the
    following list of sections: [5-8), [8-30), [30-31], so the points -32, 4.5,
    32 and 100 all match no section, while 5 and 7.5 match [5-8) and so for
    them the function returns 5, and 30, 30.7 and 31 all match [30-31].

    Parameters
    ---------
    point : float
        The point for which to match a section.
    section_list : sortedcontainers.SortedList
        A list of start points of consecutive sections.

    Returns
    -------
    float
        The start of the section the given point belongs to. None if no match
        was found.

    Example
    -------
    >>> from sortedcontainers import SortedList
    >>> seclist = SortedList([5, 8, 30, 31])
    >>> find_point_in_section_list(4, seclist)

    >>> find_point_in_section_list(5, seclist)
    5
    >>> find_point_in_section_list(27, seclist)
    8
    >>> find_point_in_section_list(31, seclist)
    30
    """
    if point < section_list[0] or point > section_list[-1]:
        return None
    if point in section_list:
        if point == section_list[-1]:
            return section_list[-2]
        ind = section_list.bisect(point)-1
        if ind == 0:
            return section_list[0]
        return section_list[ind]
    try:
        ind = section_list.bisect(point)
        return section_list[ind-1]
    except IndexError:
        return None


def find_range_ix_in_section_list(start, end, section_list):
    """Returns the index range all sections belonging to the given range.

    The given list is assumed to contain start points of consecutive
    sections, except for the final point, assumed to be the end point of the
    last section. For example, the list [5, 8, 30, 31] is interpreted as the
    following list of sections: [5-8), [8-30), [30-31]. As such, this function
    will return [5,8] for the range (7,9) and [5,8,30] while for (7, 30).

    Parameters
    ---------
    start : float
        The start of the desired range.
    end : float
        The end of the desired range.
    section_list : sortedcontainers.SortedList
        A list of start points of consecutive sections.

    Returns
    -------
    iterable
        The index range of all sections belonging to the given range.

    Example
    -------
    >>> from sortedcontainers import SortedList
    >>> seclist = SortedList([5, 8, 30, 31])
    >>> find_range_ix_in_section_list(3, 4, seclist)
    [0, 0]
    >>> find_range_ix_in_section_list(6, 7, seclist)
    [0, 1]
    >>> find_range_ix_in_section_list(7, 9, seclist)
    [0, 2]
    >>> find_range_ix_in_section_list(7, 30, seclist)
    [0, 3]
    >>> find_range_ix_in_section_list(7, 321, seclist)
    [0, 3]
    >>> find_range_ix_in_section_list(4, 321, seclist)
    [0, 3]
    """
    if start > section_list[-1] or end < section_list[0]:
        return [0, 0]
    if start < section_list[0]:
        start_section = section_list[0]
    else:
        start_section = find_point_in_section_list(start, section_list)
    if end > section_list[-1]:
        end_section = section_list[-2]
    else:
        end_section = find_point_in_section_list(end, section_list)
    return [
        section_list.index(start_section), section_list.index(end_section)+1]


def find_range_in_section_list(start, end, section_list):
    """Returns all sections belonging to the given range.

    The given list is assumed to contain start points of consecutive
    sections, except for the final point, assumed to be the end point of the
    last section. For example, the list [5, 8, 30, 31] is interpreted as the
    following list of sections: [5-8), [8-30), [30-31]. As such, this function
    will return [5,8] for the range (7,9) and [5,8,30] while for (7, 30).

    Parameters
    ---------
    start : float
        The start of the desired range.
    end : float
        The end of the desired range.
    section_list : sortedcontainers.SortedList
        A list of start points of consecutive sections.

    Returns
    -------
    iterable
        The starting points of all sections belonging to the given range.

    Example
    -------
    >>> from sortedcontainers import SortedList
    >>> seclist = SortedList([5, 8, 30, 31])
    >>> find_range_in_section_list(3, 4, seclist)
    []
    >>> find_range_in_section_list(6, 7, seclist)
    [5]
    >>> find_range_in_section_list(7, 9, seclist)
    [5, 8]
    >>> find_range_in_section_list(7, 30, seclist)
    [5, 8, 30]
    >>> find_range_in_section_list(7, 321, seclist)
    [5, 8, 30]
    >>> find_range_in_section_list(4, 321, seclist)
    [5, 8, 30]
    """
    ind = find_range_ix_in_section_list(start, end, section_list)
    return section_list[ind[0]: ind[1]]


def find_range_ix_in_point_list(start, end, point_list):
    """Returns the index range all points inside the given range.

    Parameters
    ---------
    start : float
        The start of the desired range.
    end : float
        The end of the desired range.
    point_list : sortedcontainers.SortedList
        A list of points.

    Returns
    -------
    iterable
        The index range of all points inside the given range.

    Example
    -------
    >>> from sortedcontainers import SortedList
    >>> point_list = SortedList([5, 8, 15])
    >>> find_range_ix_in_point_list(3, 4, point_list)
    [0, 0]
    >>> find_range_ix_in_point_list(3, 7, point_list)
    [0, 1]
    >>> find_range_ix_in_point_list(3, 8, point_list)
    [0, 2]
    >>> find_range_ix_in_point_list(4, 15, point_list)
    [0, 3]
    >>> find_range_ix_in_point_list(4, 321, point_list)
    [0, 3]
    >>> find_range_ix_in_point_list(6, 321, point_list)
    [1, 3]
    """
    return [point_list.bisect_left(start), point_list.bisect_right(end)]
