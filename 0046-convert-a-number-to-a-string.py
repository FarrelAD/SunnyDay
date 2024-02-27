# TITLE: FIND THE NEXT PERFECT SQUARE
# TASK : You might know some pretty large perfect squares. But what about the NEXT one?
#        Complete the findNextSquare method that finds the next integral perfect square after the one passed
#        as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
# Source: https://www.codewars.com/kata/56269eb78ad2e4ced1000013
# 27 February 2024

# 1st method
# def number_to_string(num):
#     string_of_num = str(num)
#     return string_of_num

# 2nd method
# def number_to_string(num):
#     return str(num)

# 3rd method
number_to_string = lambda num: str(num)

# Testing
print(number_to_string(999))
print(type(number_to_string(999)))

print(number_to_string(12145))
print(type(number_to_string(12145)))