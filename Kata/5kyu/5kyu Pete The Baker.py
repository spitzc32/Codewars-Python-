"""
    created By: Neet/ Spitcz32
    
"""

def cakes1L(recipe, available):
    return min([0 if ingridient not in available or recipe[ingridient]//available[ingridient] < 0 else available[ingridient]//recipe[ingridient] for ingridient in recipe])

def cakes(recipe, available):
    nums = []
    for ingridient in recipe:
        if ingridient not in available or recipe[ingridient]//available[ingridient] < 0:
            print ("passing here")
            return 0
        else: 
            nums.append(available[ingridient]//recipe[ingridient])
    
    return min(nums)
