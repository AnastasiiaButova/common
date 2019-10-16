import math

def code_two_list(list_1, list_2):
    c = set(list_1) & set(list_2)
    return list(c)

'''Task 2:
Return the number of times that the letter “a” appears anywhere in the given string
Given string is “I am a good developer. I am also a writer” and output should be 5.'''

def code_str():
    sentence = "I am a good developer.I am also a writer"
    return sentence.count('a')

def three(num):
    a = math.log(num, 3)
    if a == int(a):
        return True

def add_digits(num):
    while True:
        digits_count = sum(int(digit) for digit in str(num))
        if digits_count <=9:
            return digits_count
        num = digits_count

'''Task 5:
Write a Python program to push all zeros to the end of a list.

Input : [0,2,3,4,6,7,10]
Output : [2, 3, 4, 6, 7, 10, 0]'''

def zero_end(l):
    result = l[::-1]
    a = 0
    for i in l:
        if i == 0:
            l.remove(i)
            l.append(0)
        a +=1
    return l


'''Task 6:
Write a Python program to check a sequence of numbers is an arithmetic progression or not.
Input : [5, 7, 9, 11]
Output : True'''

def arithmetic_progression(a):
    difference = a[1] - a[0]
    for i in range(len(a) - 1):
        if a[i + 1] - difference != a[i]:
            return False
    return True

'''Task 7:
Write a Python program to find the number in a list that doesn't occur twice.
Input : [5, 3, 4, 3, 4]
Output : 5'''

def unique_num(numbers):
    a = 0
    for i in numbers:
        a ^= i
    return a

'''Task 8:
Write a Python program to find a missing number from a list.
Input : [1,2,3,4,6,7,8]
Output : 5'''

def missing(numbers):
    return sum(range(numbers[0],numbers[-1]+1)) - sum(numbers)

'''Task 9:
Write a Python program to count the elements in a list until an element is a tuple.

Sample Test Cases:
Input: [1,2,3,(1,2),3]
Output: 3'''

def count(numbers):
    count = 0
    for i in numbers:
        if isinstance(i, tuple):
            break
        count += 1
    return count

'''Task 10:
Write a program that will take the str parameter being passed and return the string in reversed order. 
For example: if the input string is "Hello World and Coders" then your program should return the string sredoC dna dlroW olleH.'''

def reverse_string(sentence):
    reversed_sent = ''.join(reversed(sentence))
    return reversed_sent

    pass