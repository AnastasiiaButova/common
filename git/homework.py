"""
This is a list of functions that should be completed.
"""

from typing import Any
from typing import List


class OurAwesomeException(Exception):
    pass


def is_two_object_has_same_value(a,b) -> bool:
    """
    If @first and @second has same value should return True
    In another case should return False
    """
    if a == b:
        return True
    else:
        return False
   


def is_two_objects_has_same_type(a,b) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    if type(a) == type(b):
        return True
    else:
        return False



def is_two_objects_is_the_same_objects(a,b) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    if a is b:
        return True
    else:
        return False



def multiple_ints(a,b) -> int:
    """
    Should calculate product of all args.
    if first_value or second_value is not int should raise ValueError

    Raises:
        ValueError

    Params:
        first_value: value for multiply
        second_value
    Returns:
        Product of elements
    """
    if type(a) != int or type(b) != int:
        raise ValueError('Alarma! Something is not an integer')
    else:
        return a * b
    


def multiple_ints_with_conversion(a,b) -> int:
    """
    If possible to convert arguments to int value - convert and multiply them.
    If it is impossible raise ValueError

    Args:
        first_value: number for multiply
        second_value: number for multiply

    Raises:
        ValueError

    Returns: multiple of two numbers.

    Examples:
        multiple_ints_with_conversion(6, 6)
        >>> 36
        multiple_ints_with_conversion(2, 2.0)
        >>> 4
        multiple_ints_with_conversion("12", 1)
        >>> 12
        try:
            multiple_ints_with_conversion("Hello", 2)
        except ValueError:
            print("Not valid input data")
        >>> "Not valid input data"
    """
    if type((a) is float or int) and (type(b) is float or int):
        a_int = int(a)
        b_int = int(b)
        return a_int * b_int
    elif a.isdigit() or b.isdigit():
        a = float(a)
        b = float(b)
        a_int = int(a)
        b_int = int(b)
        return a_int * b_int
    else:
        raise ValueError('Not valid input data')
    


def is_word_in_text(word,text) -> bool:
    """
    If text contain word return True
    In another case return False.

    Args:
        word: Searchable substring
        text: Text for searching

    Examples:
        is_word_in_text("Hello", "Hello word")
        >>> True
        is_word_in_text("Glad", "Nice to meet you ")
        >>> False

    """
 
    if word in text:
        return True
    else:
        return False
    


def some_loop_exercise() -> list:
    """
    Use loop to create list that contain int values from 0 to 12 except 6 and 7
    """
    return [i for i in range(13) if i !=6 and i !=7]    


def remove_from_list_all_negative_numbers(l: List[int]) -> list:
    """
    Use loops to solve this task.
    You could use data.remove(negative_number) to solve this issue.
    Also you could create new list with only positive numbers.
    Examples:
        remove_from_list_all_negative_numbers([1, 5, -7, 8, -1])
        >>> [1, 5, 8]
    """
    return [i for i in l if i>= 0]
    


def alphabet() -> dict:
    """
    Create dict which keys is alphabetic characters. And values their number in alphabet
    Notes You could see an implementaion of this one in test, but create another one
    Examples:
        alphabet()
        >>> {"a": 1, "b": 2 ...}
    """
    import string
    i = 0
    for c in string.ascii_lowercase:
        i = i + 1
        d = {i: c}
        return d
  


def simple_sort(data: List[int]) -> List[list]:
    """
    Sort list of ints without using built-in methods.
    Examples:
        simple_sort([2, 9, 6, 7, 3, 2, 1])
        >>> [1, 2, 2, 3, 6, 7, 9]
    Returns:

    """
    l = []
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l

    print("Done!")
