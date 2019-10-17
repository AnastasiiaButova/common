import math
import string
import pytest
import mock
import builtins

'''Task 11:
Write a program that will take the num parameter being passed and return the number of hours and minutes
the parameter converts to (ie. if num = 63 then the output should be 1:3). Separate the number of hours and minutes with a colon.cd
'''

def time_convert(num):
        hours = int(math.floor(num / 60))
        minutes = num % 60
        return str(hours) + ':' + str(minutes)

def test_time_convert():
    assert time_convert(63) == '1:3'

'''Task 12:
Write a program that will take the parameter being passed and return the largest word in the string. 
If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation.
Sample Test Cases:
Input:"fun&!! time"
Output:time

Input:"I love dogs"
Output:love'''

def longest_word(sentence):
    sentence = ''.join([c for c in sentence if c not in ('!', '?','&')])
    word = sentence.split(' ')
    return (max(word, key=len))

@pytest.mark.parametrize("test_input,expected",
                         [('fun&!! time', 'time'), ('I love dogs', 'love')])
def test_longest_word(test_input,expected):
    assert longest_word(test_input) == expected


'''Task 13:
Write a program (using functions!) that asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order.

For example:
Input: My name is Michele
Outout: Michele is name My'''


def backwards():
    sentence = input('Please, enter the sentence: ')
    for line in sentence.split('\n'):
        return ' '.join(line.split()[::-1])


def test_backwards():
    with mock.patch.object(builtins, 'input', lambda _: 'My name is Michele'):
        assert backwards() == 'Michele is name My'


'''Task 14:       
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to generate.'''


def fibonacci():
    numbers = int(input('How many Fibonacci numbers to generate : '))
    a, b = 0, 1
    while b < numbers:
        a, b = b, a + b
        return b


#def test_fibonnaci():
#    with pytest.raises(ValueError):
#        fibonnaci(-1)

def test_fibonacci():
    with mock.patch('builtins, input', return_value = 6):
        assert fibonacci() == [1, 1, 2, 3, 5, 8]




#class FibonacciTests(TestCase):
#    def test_returns_correct_fibonacci_number(self):
#        correct_sequence = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
#        for index in range(len(correct_sequence)):
#            response = fibonacci(index)
#            assert response == correct_sequence[index]
