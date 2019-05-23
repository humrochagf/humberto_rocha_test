def version_str_to_tuple(version):
    """Convert a version string into a tuple

    Parameters
    ----------
    version : str
        The dot separated version string: '1.2.0'

    Return
    ------
    tuple
        A tuple of integers with the version: (1, 2, 0)

    """
    return tuple(map(int, version.split('.')))


def cmp_version(v1, v2):
    """Compare two version strings

    Version strings are composed by numbers
    separated by dot like '1.2.0'

    Parameters
    ----------
    v1 : str
        The first version string
    v2 : str
        The second version string

    Returns
    -------
    int
        1 if v1 > v2
        0 if v1 == v2
        -1 if v1 < v2
    """
    v1 = version_str_to_tuple(v1)
    v2 = version_str_to_tuple(v2)

    return (v1 > v2) - (v2 > v1)
