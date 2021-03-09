from string_calculator import add


def test_empty():
    actual = add("")
    expected = 0
    assert actual == expected


def test_single_nr():
    for nr in ['0', '1', '12', '-1', '-12']:
        actual = add(nr)
        expected = int(nr)
        assert actual == expected


def test_multi_nrs():
    actual = add('1,2,3')
    expected = 6
    assert actual == expected


def test_multi_nrs_not_int():  # to fail
    actual = add('1.1,2.2,3.3')
    expected = 6.6
    assert actual == expected


def test_int_input():  # to fail - user input is str
    actual = add(1)
    expected = 3
    assert actual == expected


def test_non_numeric_input():
    actual = add('a,b,c')
    expected = 0
    assert actual == expected
