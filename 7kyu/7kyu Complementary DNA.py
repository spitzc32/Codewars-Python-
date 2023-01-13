"""
    Created by: Neet/ Spitcz32
    
"""

def DNA_strand(dna):
    com = {'A':'T','T':'A','C':'G','G':'C'}
    return ''.join([com[val] for val in list(dna)])
