"""
    Created by: Neet/Spitcz32

    
"""


from functools import reduce
def bin_to_decimal(inp):
    return reduce(lambda x, y: x + y,[int(x) * 2 ** y for x, y in zip(list(inp), range(len(inp) - 1, -1, -1))])
