# TITLE: ISOGRAMS
# TASK : An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
#        Implement a function that determines whether a string that contains only letters is an isogram.
# Source: https://www.codewars.com/kata/54a91a4883a7de5d7800009c
# 11 March 2024

# 1st method
def is_isogram(string):
    new_str = string.lower()
    temp_char = []
    for char in new_str:
        if char in temp_char:
            return False
        temp_char.append(char)
        
    return True
    

# Testing
print(is_isogram('moose'))
print(is_isogram('moOse'))
print(is_isogram('Dermatoglyphics'))
print(is_isogram(''))
print(is_isogram('isogram'))