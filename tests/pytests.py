import math
import string
import pytest


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

def test_1_longest_word():
    assert longest_word('fun&!! time') == 'time'

def test_2_longest_word():
    assert longest_word('I love dogs') == 'love'

'''Task 13:
Write a program (using functions!) that asks the user for a long string containing multiple words. 
Print back to the user the same string, except with the words in backwards order.

For example:
Input: My name is Michele
Outout: Michele is name My'''


def backwards(sentence):
    sentence = input('Please, enter the sentence: ')
    sentence = sentence.split(' ')
    output = ' '.join(sentence)
    return output

def test_backwards():
    assert backwards('My name is Michele') == 'Michele is name My'
