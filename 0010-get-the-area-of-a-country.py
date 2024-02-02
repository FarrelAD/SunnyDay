# TITLE: GET THE AREA OF A COUNTRY
# TASK : Create a function that takes a country's name and its area as arguments 
#        and returns the area of the country's proportion of the total world's landmass.
# Source: https://edabit.com/challenge/Cjtm4CpLzHDerQMfX
# 2 February 2024

# Function to get the proportion of a country's area
# 1st method - basic function
# def area_of_country(name, area):
#     world_landmass = 148940000
#     country_area_proportion = round(area / world_landmass * 100, 2)
#     output = f"{name} is {country_area_proportion}% of the total world\'s landmass"
#     return output

# 2nd method 
# def area_of_country(name, area):
#     return f"{name} is "+str(round(area / 148940000 * 100, 2))+"% of the total world\'s landmass"

# 3rd method - lambda function
area_of_country = lambda name, area: f"{name} is "+str(round(area / 148940000 * 100, 2))+"% of the total world\'s landmass"

# For Python 3.4 version
# def area_of_country(name, area):
#     world_landmass = 148940000
#     country_area_proportion = area / world_landmass * 100
#     return "{} is {:.2f}% of the total world's landmass".format(name, country_area_proportion)

print(area_of_country('Russia', 17098242))
print(area_of_country('USA', 9372610))
print(area_of_country('Iran', 1648195))
print(area_of_country('China', 9706961))