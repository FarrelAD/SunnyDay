# TITLE: FIND THE NEXT PERFECT SQUARE
# TASK : You might know some pretty large perfect squares. But what about the NEXT one?
#        Complete the findNextSquare method that finds the next integral perfect square after the one passed
#        as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
# Source: https://www.codewars.com/kata/56269eb78ad2e4ced1000013
# 26 February 2024

# 1st method
# import math

# def find_next_square(sq):
#     square_side = math.sqrt(sq)
#     next_square = -1

#     if square_side.is_integer():
#         next_square = math.pow(square_side + 1, 2)

#     return next_square

# 2nd method - without using math library
# def find_next_square(sq):
#     square_side = sq**0.5
#     next_square = -1

#     if square_side.is_integer():
#         next_square = (square_side + 1)**2
    
#     return next_square

# 3rd method
# def find_next_square(sq):
#     next_square = ((sq**0.5) + 1)**2 if (sq**0.5).is_integer() else -1
#     return next_square

# 4th method - ONE LINE!!
find_next_square = lambda sq: ((sq**0.5) + 1)**2 if (sq**0.5).is_integer() else -1


# Testing
print(find_next_square(121))
print(find_next_square(625))
print(find_next_square(135))