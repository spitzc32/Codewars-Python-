"""
    Created by: Neet/Spitcz32

    
"""

def evaporator(content, evap_per_day, threshold):
    i = 0
    curr = content
    while curr >= content * threshold / 100.0:
        curr = curr * (1-evap_per_day/100.0)
        print(curr)
        i += 1
    return i
