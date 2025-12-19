# print hello world
print(f"Hello world!")

# get user name input remove the white spaces and capitalize the first letter of each word
# atrip removes white spaces from the beginning and end of the string
# title capitalizes the first letter of each word
name = input("What is your name? ").strip().title()

# print the name of user
print(f"Hello {name}")

# get user Age input and convert it to a integer
age = int(input("How old are you? "))

# print the Age of the user
print(f"You are {age} years old.")