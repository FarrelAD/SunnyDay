# TITLE: COUNTING DUPLICATES
# TASK : Write a function that will return the count of distinct case-insensitive alphabetic characters 
#        and numeric digits that occur more than once in the input string. The input string can be assumed to 
#        contain only alphabets (both uppercase and lowercase) and numeric digits.
# Source: https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
# 11 February 2024

# Function to count duplicates of the alphabet
# 1st method
# def duplicate_count(text):
#     # Convert from string to a list of char
#     char_of_text = []
#     for i in text:
#         char_of_text += [i.lower()]
    
#     # Define unduplicated char in a list
#     char_set = set(char_of_text)
    
#     # Count the duplicate of char
#     duplicate_char = []
#     for i in char_set:
#         count_char = 0
#         for j in char_of_text:
#             if j == i:
#                 count_char += 1

#         if (i in char_of_text) and (count_char > 1):
#             duplicate_char += [i]

#     # Count the length or the amount of duplicate char
#     len_of_duplicate_char = len(duplicate_char)
#     return len_of_duplicate_char

# 2nd method - more short
def duplicate_count(text):
    char_set = set(text.lower())
    duplicate_char = []
    for i in char_set:
        count_char = 0
        for j in text: count_char += 1 if j == i else 0
        
        duplicate_char += [i] if (i in text) and (count_char > 1) else []

    return len(duplicate_char)

# Testing
print(duplicate_count('Indivisiblities'))
print(duplicate_count('Economy'))
print(duplicate_count('Responsibilities'))