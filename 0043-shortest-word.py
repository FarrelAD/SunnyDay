# TITLE: SHORTEST WORD
# TASK : Simple, given a string of words, return the length of the shortest word(s).
#        String will never be empty and you do not need to account for different data types.
# Source: https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9
# 25 February 2024

# 1st method
# def find_short(s):
    # splitted_string = []
    # curr_char = temp_string = ''
    # for index, char in enumerate(s):
    #     curr_char = char

    #     if index == len(s) - 1:
    #         temp_string += char

    #     if curr_char == ' ' or index == len(s) - 1:
    #         splitted_string.append(temp_string)
    #         temp_string = ''
    #     else:
    #         temp_string += char
    
    # word_length = [len(word) for word in splitted_string]

    # shortest_word = temp_word_length  = 0
    # for index, char in enumerate(word_length):
    #     temp_word_length = char
    #     if index == 0:
    #         shortest_word = char
        
    #     if temp_word_length < shortest_word: 
    #         shortest_word = temp_word_length

    # return shortest_word

# 2nd method
# def find_short(s):
#     splitted_string = s.split()
    
#     word_length = [len(word) for word in splitted_string]

#     shortest_word = min(word_length)
#     return shortest_word

# 3rd method
# def find_short(s):
#     word_length = [len(word) for word in s.split()]
#     return min(word_length)

# 4th method
# def find_short(s):
#     return min([len(word) for word in s.split()])

# 5th method - ONE LINE! Lambda function
find_short = lambda s: min([len(word) for word in s.split()])


# Testing
print(find_short("bitcoin take over the world maybe who knows perhaps")) # 3
print(find_short("i want to travel the world writing code one day")) # 1
print(find_short("lets talk about javascript the best language")) # 3