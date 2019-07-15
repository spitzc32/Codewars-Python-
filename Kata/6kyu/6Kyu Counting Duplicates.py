from collections import Counter
def duplicate_count(text):
    return len([group for key, group in Counter(list(text.lower())).items() if group > 1])
    
