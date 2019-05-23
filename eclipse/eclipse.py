from collections import namedtuple

Line = namedtuple('Line', ['x1', 'x2'])


def is_overlapping(line1, line2):
    """Given two lines and return True if they overlap or False if not"""
    return max(line1) >= min(line2) and max(line2) >= min(line1)
