# TITLE: PETE, THE BAKER
# TASK : Pete likes to bake some cakes. He has some recipes and ingredients. 
#        Unfortunately he is not good in maths. Can you help him to find out, how many cakes he could bake considering his recipes?
# Source: https://www.codewars.com/kata/525c65e51bf619685c000059
# 1 March 2024

# 1st method
# import math

# def cakes(recipe, available):
#     # Checking all recipe key in available dict
#     for key in recipe.keys():
#         if key not in available:
#             return 0
            
#     # Divie all the available ingredients with recipe 
#     result = []
#     for i, key in enumerate(recipe.keys()):
#         result.append(math.floor(available[key] / recipe[key]))

#     # Check the lowest value from the result and then return it
#     return min(result)


# 2nd method
import math

def cakes(recipe, available):
    for key in recipe.keys():
        if key not in available: return 0

    return min([math.floor(available[key] / recipe[key]) for key in recipe.keys()])

# Testing
print(
    cakes(
        {
            'flour': 500, 
            'sugar': 200, 
            'eggs': 1
        }, 
        
        {
            'flour': 1200, 
            'sugar': 1200, 
            'eggs': 5, 
            'milk': 200
        }
    )
)

print(
    cakes(
        {
            'apples': 3, 
            'flour': 300, 
            'sugar': 150, 
            'milk': 100, 
            'oil': 100
        }, 

        {
            'sugar': 500, 
            'flour': 2000, 
            'milk': 2000
        }
    )
)