# TITLE: CIRCLE OR SQUARE?
# TASK : Give 'TRUE' value IF THE CIRCUMFERENCE OF THE CIRCLE IS GREATER
#        than square's perimeter. Give 'FALSE' value IF THE 
#        SQUARE'S PERIMETER IS GREATER than the circumference of the circle
# Source: https://edabit.com/challenge/4me7LifXBwj5rhL4n
# 1 February 2024

# Function to check value of circle and square
# 1st method - basic function 
# def circle_or_square(rad, area):
# 	phi: float = 3.14
# 	square_side: int = area**0.5
# 	circle_circumference: float = 2 * phi * rad
# 	square_perimeter: int = square_side * 4
# 	if circle_circumference > square_perimeter:
# 		return True
# 	else:
# 		return False
	
# 2nd method
# def circle_or_square(rad, area):
# 	if (2 * 3.14 * rad) > (area**0.5 * 4):
# 		return True
# 	else:
# 		return False
	
# 3rd method - shorthand if else
# def circle_or_square(rad, area):
#     return (2 * 3.14 * rad) > (area**0.5 * 4)

# 4th method - lambda function
# circle_or_square = lambda rad, area : (2 * 3.14 * rad) > (area**0.5 * 4)

# 5th method - using math modules and lambda function
import math

# math.tau is equal to 2 * phi
# math.sqrt(x) is to get the value of square root of x
circle_or_square = lambda rad, area : (math.tau * rad) > (math.sqrt(area) * 4)


print(circle_or_square(16, 625))
print(circle_or_square(5, 100))
print(circle_or_square(8, 144))