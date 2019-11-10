import math

'''Task 11:
Write a program that will take the num parameter being passed and return the number of hours and minutes
the parameter converts to (ie. if num = 63 then the output should be 1:3). Separate the number of hours and minutes with a colon.cd
'''


def time_convert(num):
    hours = int(math.floor(num / 60))
    minutes = num % 60
    return str(hours) + ':' + str(minutes)


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
    return max(word, key=len)


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


'''Task 14:       
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to generate.'''


def fibonacci():
    numbers = int(input('How many Fibonacci numbers to generate : '))
    if numbers <= 0:
        raise ValueError("Please, integer should be above 0")
    a, b = 1, 1
    fibo = [a,b]
    while b < numbers:
        a, b = b, a + b
        fibo.append(b)
    return fibo


'''Task 15:       
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.'''


def even_list(lst):
    return [i for i in lst if i % 2 == 0]


'''Task 16:       
Write a program that will add up all the numbers from 1 to input number. 
For example: if the input is 4 then your program should return 10 because 1 + 2 + 3 + 4 = 10. '''


def sum_up():
    numbers = int(input('Please, enter the integer: '))
    return sum(range(1, numbers+1))


'''Task 17:       
Write a program that will take the parameter being passed and return the factorial of it. 
For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24.'''


def factorial_digit(a):
    return math.factorial(a)


'''Task 18:       
Write a program that will take the str parameter being passed and modify it using the following algorithm. 
Replace every letter in the string with the letter following it in the alphabet (ie. cbecomes d, zbecomes a). 
Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string.
Input: abcd
Output: bcdE '''


def string_modify(letters):
    vowels = set('aeiou')
    final_lst = []
    for i in letters:
        if i.isalpha():
            new_i = 'a' if i.lower() == 'z' else chr(ord(i) + 1)
            if new_i in vowels:
                new_i = new_i.upper()
        else:
            new_i = i
        final_lst.append(new_i)
    return"".join(final_lst)


'''Task 19:       
Write a program that will take the str string parameter being passed and return the string with the letters in alphabetical order 
(ie. hello becomes ehllo). Assume numbers and punctuation symbols will not be included in the string.
Input: edcba
Output: abcde'''


def alpha_order(letters):
    punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~1234567890'''
    clear_lst = ""
    for i in letters:
        if i not in punctuations:
            clear_lst = clear_lst + i
    return "".join(sorted(clear_lst))


'''Task 20:       
Write a program that will take both parameters being passed and return the true if num2 is greater than num1, 
otherwise return the false. If the parameter values are equal to each other then return the string -1'''


def logic(a,b):
    if a < b:
        return True
    if a == b:
        return '-1'
    if a > b:
        return False



