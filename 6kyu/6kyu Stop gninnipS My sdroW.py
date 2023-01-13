"""
    Created by: Neet/ Spitcz32
    
"""

def spin_words(sentence):
    return ' '.join([c[::-1] if len(c)>=5 else c for c in sentence.split()])
