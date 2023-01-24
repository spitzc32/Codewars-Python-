""" Created by: SNeet/Spitcz32

    5 kyu: Product of consecutive Fib numbers

    Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying

    F(n) * F(n+1) = prod.

    Your function productFib takes an integer (prod) and returns an array:

    [F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
    depending on the language if F(n) * F(n+1) = prod.

    If you don't find two consecutive F(m) verifying F(m) * F(m+1) = prodyou will return

    [F(m), F(m+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
    F(m) being the smallest one such as F(m) * F(m+1) > prod.



"""

import math as m

def productFib(prod):
    """
        param: prod - matching 2 consecutive fibonacci number

        returns a list containing 2 consecutive numbers and a boolean exp. if prod is
        equal to the product of the 2 consecutive numbers
    """
    a,b = 0,1
    for i in range(int(m.sqrt(prod))): 
        a,b = b,a+b
        if a*b >= prod: break 
         
    return [a,b,True] if a*b == prod else [a,b,False]

def productFib(prod):
    a,b = 0,1
    
    for i in range(int(m.sqrt(prod))):
        a,b = b, a+b
        if a*b > prod:
            return [a,b,False]
        elif a*b == prod:
            return [a,b,True]
    return 0 
