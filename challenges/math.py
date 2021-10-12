from typing import List


def question_1(x: int, y: int) -> List[int]:
    '''
    Write a function that takes two integers (x and y) and returns a list of numbers between x and y that are divisible by 5 but not by 7.

    Answer = Bewteen x and y is a key factor, thus, this is a not inclusive range, x and y cannot be in list. Look into range(x, y) in order to
    not return y in the list if the condition is met (not inclusive range).
    '''
    return [q for q in range(x, y) if q%5 == 0 and q%7 != 0]

def question_2() -> str:
    '''
    Write a function that takes two numbers (x and y) as input and returns the value to the following function:
    
    Answer = There is not funtcion in the pdf. I assume it refers to function 3, for this, instead of taking two arguments, 
    I will make use of python built-in inputs to built a CLI and then call function 3.
    '''
    x = input('Give me a number to be converted: ')
    b = input('To which base shoul I convert it (0-9): ')

    number: str = question_3(x, b)

    return number

def question_3(x: int, b: int) -> str:
    '''
    Write a function that takes two integers (x and b) as inputs and returns a string that represents the number x in base b
    Example 1: if x=5 and b=2 then the function will return "101"
    Example 2: if x=5 and b=3 then the function will return "12"

    Answer = given x (the number to be converted) and the base (b), the number will be divided by the base, if the number residue is 0,
    then a 0 will be append to a list, if not then the residue will be appended. This operation will be performed until reaching one.
    Then the list will be flipped. This technique is used in binary, hexadecimal conversions and works for any base, but in this 
    case will be limited to a base of 9 in order to avoid working with letters.
    '''
    if x == 0:
        return '0'
    number: str = ''
    while x:
        if x%b == 0:
            number += str(0)
            x //= b
        else:
            number += str(x%b)
            x //= b
    return number[::-1]