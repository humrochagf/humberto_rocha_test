from themis import cmp_version, version_str_to_tuple


def test_version_str_to_tuple():
    assert version_str_to_tuple('1.2.3') == (1, 2, 3)


def test_cmp_version_greater_than():
    assert cmp_version('1.1', '1.0') == 1


def test_cmp_version_lower_than():
    assert cmp_version('1.0', '1.1') == -1


def test_cmp_version_equals():
    assert cmp_version('1.0', '1.0') == 0


def test_cmp_version_different_lengths():
    assert cmp_version('1.2.3', '1.2') == 1


def test_cmp_version_string_corner_case():
    """If you compare it as strings you will get a wrong answer"""
    assert cmp_version('1.10', '1.2') == 1
