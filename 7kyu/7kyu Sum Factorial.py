"""
    Created by: Neet/ Spitcz32
    
"""

from functools import reduce

def sum_factorial(lst):
    return sum([reduce((lambda x, y: x * y), range(1,i+1)) for i in lst])
