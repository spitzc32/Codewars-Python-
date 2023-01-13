"""
`created by: SNeet/spitcz32

    
"""
from functools import reduce


def get_expo(num):
    if num <= 4: return num
    t = num % 100 if num % 100 > 1 else num % 1000
    exp = 4 if t % 4 == 0 else t % 4
    result = exp if exp > 1 else t
    return result


def last_digit(numbers):
    if not numbers: return 1
    if len(numbers) == 1: return numbers[0] % 10
    expo = numbers[1] if len(numbers) == 2 else reduce(lambda y, x: x ** get_expo(y), numbers[1:][::-1])
    return ((numbers[0] % 10) ** get_expo(expo)) % 10


"""

def last_digit(lst):
    n = 1
    for x in reversed(lst):
        n = x ** (n if n < 4 else n % 4 + 4)
    return n % 10

"""
    

