import pytest
import mock
import builtins
from tests.hw_5_11_20 import (time_convert,
                              longest_word,
                              backwards,
                              fibonacci,
                              even_list,
                              sum_up,
                              factorial_digit,
                              string_modify,
                              alpha_order,
                              logic
                              )


def test_time_convert():
    assert time_convert(63) == '1:3'

@pytest.mark.parametrize("test_input,expected",
                         [('fun&!! time', 'time'), ('I love dogs', 'love')])
def test_longest_word(test_input,expected):
    assert longest_word(test_input) == expected


def test_backwards():
    with mock.patch.object(builtins, 'input', lambda _: 'My name is Michele'):
        assert backwards() == 'Michele is name My'


def test_fibonacci_value_error():
    with mock.patch.object(builtins, 'input', lambda _: -5):
        with pytest.raises(ValueError, match="Please, integer should be above 0" ):
            fibonacci()


def test_fibonacci():
    with mock.patch.object(builtins, 'input', lambda _: 6):
        assert fibonacci() == [1, 1, 2, 3, 5, 8]


def test_even_list():
    assert even_list([1, 4, 9, 16, 25, 36, 49, 64, 81, 100]) == [4, 16, 36, 64, 100]


def test_sum_up():
    with mock.patch.object(builtins, 'input', lambda _: 4):
        assert sum_up() == 10


def test_factorial_digit():
    assert factorial_digit(4) == 24


def test_string_modify():
    assert string_modify('abcd') == 'bcdE'


def test_alpha_order():
    assert alpha_order('edcba)33') == 'abcde'


def test_logic():
    assert logic(5, 6) == True
    assert logic(5, 5) == '-1'
    assert logic(6, 5) == False
