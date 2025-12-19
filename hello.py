# print hello world
print(f"Hello world!")

# get user name input remove the white spaces and capitalize the first letter of each word
# atrip removes white spaces from the beginning and end of the string
# title capitalizes the first letter of each word
name = input("What is your name? ").strip().title()

# print the name of user say hello user
print(f"Hello {name}")

name1 = input("What is your mom name? ").strip().title()
# say hello to user again but use the end and sep parameters to print on the same line
#end parameter is used to add a character at the end of the string
#sep parameter is used to add a character between the strings
print(f"Hello {name1}", end="  ", sep="  ")
# get user Age input and convert it to a integer
age = int(input("How old are you? "))

# print the Age of the user
print(f"You are {age} years old.")

# say hello to user double quotes
print('hello, "friend"')