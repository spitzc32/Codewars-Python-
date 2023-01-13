"""
    Created by: Neet/ Spitcz32
    
"""


import re

def is_valid_IP(strng):
    if (re.match("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", strng)):
        return True
    else:
        return False
