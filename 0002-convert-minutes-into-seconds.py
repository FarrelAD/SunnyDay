# Convert Minutes into Seconds
# Source: https://edabit.com/challenge/FQyaaJx7orS7tiwz8
# 31 January 2024

# Function to convert minutes into seconds
# 1st - basic function
# def convert(minutes):
#     return minutes * 60

# 2nd - lambda function
convert = lambda minutes: minutes * 60

minutes = 5
print(f'My {minutes} minute(s) is {convert(minutes)} in seconds')