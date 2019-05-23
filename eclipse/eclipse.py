from collections import namedtuple

Line = namedtuple('Line', ['x1', 'x2'])


def is_overlapping(line1, line2):
    return line1.x2 >= line2.x1 and line2.x2 >= line1.x1
