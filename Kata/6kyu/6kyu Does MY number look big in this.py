"""
    Created by: Neet/ Spitcz32
    
"""


def narcissistic( value ):
    val = list(str(value))
    assess = [int(i) for i in val]
    return (True if (sum(map(lambda x: x ** len(val), assess)) == value) else False)
