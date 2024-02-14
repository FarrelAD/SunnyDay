# TITLE: DETECT PANGRAM
# TASK : Given a string, detect whether or not it is a  pangram. 
#        Return True if it is, False if not. Ignore numbers and punctuation.
# Source: https://www.codewars.com/kata/545cedaa9943f7fe7b000048
# 14 February 2024

# Function to return if it's a pangram or not
# 1st method - too long but easy to understand
# def is_pangram(string):
#     a = b = c = d = e = f = g = h = i = j = k = l = m = n = o = p = q = r = s = t = u = v = w = x = y = z = False

#     for char in string.lower():
#         if char == 'a':
#             a = True
#         elif char == 'b':
#             b = True
#         elif char == 'c':
#             c = True
#         elif char == 'd':
#             d = True
#         elif char == 'e':
#             e = True
#         elif char == 'f':
#             f = True
#         elif char == 'g':
#             g = True
#         elif char == 'h':
#             h = True
#         elif char == 'i':
#             i = True
#         elif char == 'j':
#             j = True
#         elif char == 'k':
#             k = True
#         elif char == 'l':
#             l = True
#         elif char == 'm':
#             m = True
#         elif char == 'n':
#             n = True
#         elif char == 'o':
#             o = True
#         elif char == 'p':
#             p = True
#         elif char == 'q':
#             q = True
#         elif char == 'r':
#             r = True
#         elif char == 's':
#             s = True
#         elif char == 't':
#             t = True
#         elif char == 'u':
#             u = True
#         elif char == 'v':
#             v = True
#         elif char == 'w':
#             w = True
#         elif char == 'x':
#             x = True
#         elif char == 'y':
#             y = True
#         elif char == 'z':
#             z = True

#     list_char = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]

#     for value in list_char:
#         if value == False:
#             return False
    
#     return True

# 2nd method - use a dictionary for more simple
def is_pangram(s):
    characters_dictionary = {chr(i): False for i in range(ord('a'), ord('z')+1)}

    for char in s.lower():
        if char in characters_dictionary:
            characters_dictionary[char] = True
    
    if False in characters_dictionary.values():
        return False
    else:
        return True

# Testing
print(is_pangram('The quick, brown fox jumps over the lazy dog!'))
print(is_pangram('1bcdefghijklmnopqrstuvwxyz'))
print(is_pangram('Hello World!'))