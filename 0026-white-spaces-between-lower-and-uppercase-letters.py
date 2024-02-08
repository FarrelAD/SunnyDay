# TITLE: WHITE SPACES BETWEEN LOWER AND UPPERCASE LETTERS
# TASK : Write a function that inserts a white space between every instance of a lower character
#        followed immediately by an upper character
# Source: https://edabit.com/challenge/TCbrjfMm2dPzQDbz5
# 8 February 2024

# Function to add white space between lower and uppercase letters
# 1st method
# def insert_whitespace(txt):
#     temp_string = ''

#     prev_char = ''
#     next_char = ''
#     i = 0
#     while i < len(txt):
#         if i >= 1:
#             prev_char = txt[i - 1]
#             next_char = txt[i]

#         if prev_char.islower() and next_char.isupper():
#             temp_string += ' '

#         temp_string += txt[i]

#         i += 1
#     return temp_string

# 2nd method
def insert_whitespace(txt):
    temp_string = prev_char = next_char = ''
    i = 0
    while i < len(txt):
        if i >= 1:
            prev_char = txt[i - 1]
            next_char = txt[i]
        
        if prev_char.islower() and next_char.isupper(): temp_string += ' '

        temp_string += txt[i]
        i += 1
    return temp_string



# Testing
print(insert_whitespace("SheWalksToTheBeach"))
print(insert_whitespace("MarvinTalksTooMuch"))
print(insert_whitespace("TheGreatestUpsetInHistory"))