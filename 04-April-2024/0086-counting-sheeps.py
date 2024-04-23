# TITLE: COUNTING SHEEP...
# TASK : We need a function that counts the number of sheep present in the array (true means present).
# Source: https://www.codewars.com/kata/54edbc7200b811e956000556
# 23 April 2024

# 1st
def count_sheeps(sheep):
    result = 0
    for i in sheep:
        if i == True:
            result += 1
            
    return result

# Testing
print(count_sheeps(
    [True,  True,  True,  False,
    True,  True,  True,  True ,
    True,  False, True,  False,
    True,  False, False, True ,
    True,  True,  True,  True ,
    False, False, True,  True]
    ))