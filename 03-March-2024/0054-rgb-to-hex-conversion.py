# TITLE: RGB TO HEX CONVERSION
# TASK : Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. 
#        Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.
# Source: https://www.codewars.com/kata/513e08acc600c94f01000001
# 8 March 2024

# 1st method
import math

def rgb(r, g, b):
    # All hex value from 0 to F (15)
    hex_dict = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    
    # Add all color value to a list
    color_list = [r, g, b]
    for index, color in enumerate(color_list):
        if color > 255: 
            color_list[index] = 255
        elif color < 0:
            color_list[index] = 0
    
    hexadecimal_color = ''
    
    # Converting process to hexadecimal color value
    for color in color_list:
        quotient = 1
        remainder = 0
        iteration = 0
        temp_hex = ''
        while quotient > 0:
            if iteration == 0:
                quotient = math.floor(color / 16)
                remainder = color % 16
            else:
                remainder = quotient % 16
                quotient = 0
            iteration += 1
            
            # Holds hex values for temporary
            temp_hex += hex_dict[remainder]
        
        # Concatenate to all hex
        if len(temp_hex) == 1:
            temp_hex += '0'
        hexadecimal_color += temp_hex[::-1]
    
    return hexadecimal_color


# Testing
print(rgb(255, 255, 255))
print(rgb(254, 253, 252))
print(rgb(-20, 275, 125))
print(rgb(1, 2, 3))
print(rgb(-178 ,215 ,-76))