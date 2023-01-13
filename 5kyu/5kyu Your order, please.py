"""
    Created by: Neet/ Spitcz32
    
"""


def order(sentence):
    word={}
    for w in sentence.split():
      word.update({int(i):w for i in w if i.isdigit()})
    return " ".join([word[k] for k in sorted(word.keys())])
   
