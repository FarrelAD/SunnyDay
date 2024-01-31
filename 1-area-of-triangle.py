# Count Area of Triangle
# Source: https://edabit.com/challenge/aWLTzrRsrw7RakYrN
# 31 January 2024

# Function to count the area of triangle
# 1st method - basic function
# def tri_area(base, height):
#     return (base * height) / 2

# 2nd method - using lambda function
tri_area = lambda base, height: base * height / 2

# Input base and height then print the result
print('Area of my triangle: ', tri_area(7, 4))