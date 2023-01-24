"""
    Created by: Neet/ Spitcz32
    
"""

def yahtzee_upper(dice):
    op=[]
    for x in dice:
        op.append(dice.count(x)*x)
    j=max(op)
    return j

