# TITLE: EXES AND OHS
# TASK : Check to see if a string has the same amount of 'x's and 'o's. 
#        The method must return a boolean and be case insensitive. 
#        The string can contain any char.
# Source: https://www.codewars.com/kata/55908aad6620c066bc00002a
# 2 March 2024

# 1st method
# def xo(s):
#     if 'x' not in s.lower() and 'o' not in s.lower():
#         return True
#     else:
#         if s.lower().count('o') == s.lower().count('x'):
#             return True
#         else: 
#             return False
        
# 2nd method
# def xo(s):
#     new_s = s.lower()
#     if 'x' not in new_s and 'o' not in new_s:
#         return True
#     else:
#         return True if new_s.count('o') == new_s.count('x') else False
    
# 3rd method
def xo(s):
    new_s = s.lower()
    if 'x' not in new_s and 'o' not in new_s:
        return True
    else:
        if new_s.count('o') == new_s.count('x'):
            return True
        else: 
            return False

# Testing
print(xo("ooxx")) # true
print(xo("ooxXm")) # true
print(xo("zpzpzpp")) # true
print(xo("zzoo")) # false
print(xo("X"))