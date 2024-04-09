# TITLE: CHARACTER COUNTER
# TASK : Your job will be to make sure that each character in that word has the exact same number of occurrences. 
#        You will return true if it is valid, or false if it is not.
# Source: https://www.codewars.com/kata/56786a687e9a88d1cf00005d
# 07 April 2024

# 1st 
def validate_word(word):
    # Define unique char
    unique_char = list(set(word))
    word_dict = {}
    for i in range(len(unique_char)):
        word_dict[unique_char[i]] = 0
    
    # Count all unique char
    for i in unique_char:
        for j in word:
            if j.lower() == i.lower():
                word_dict[i] += 1
    
    # Check if all the amount char is same
    first_value_dict = next(iter(word_dict.values()))
    for value in word_dict.values():
        if value != first_value_dict:
            return False
        
    return True


# Testing
print(validate_word('abcabc')) # true
print(validate_word('abcabcd')) # false