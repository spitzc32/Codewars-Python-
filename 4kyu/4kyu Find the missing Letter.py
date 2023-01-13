"""
    Created by: Neet/Spitcz32

    first Solution
    def find_missing_letter(chars):
        for i in range(len(chars)):
            if ord(chars[i+1]) - ord(chars[i]) != 1:
                return chr(ord(chars[i]) + 1)
   
"""
#One liner
def find_missing_letter(c):
    return ''.join([chr(ord(c[i])+1) for i in range(len(c)-1) if  ord(c[i+1]) - ord(c[i]) != 1])
