# In programming, conditionals are like a fork in the road. They allow your code to make decisions based on whether a condition is True or False.
# the symbols for conditionals in Python are: ==, !=, >, <, >=, <=
# The "if" statement is used to execute a block of code if a specified condition is true.
# The "else" statement is used to execute a block of code if the specified condition is false.
# The "elif" (short for "else if") statement is used to check multiple conditions in sequence.


# Boolean values in Python are True and False. They are often used in conditionals to determine the flow of a program.
# print what the user is x from user
x = int(input("What is the value of x? "))
# print what the user is y from user
y = int(input("What is the value of y? "))
# check if x is less than y
if x < y:
    print("x is less than y")
# check if x is greater than y
if x > y:
    print("x is greater than y")    
# check if x is equal to y
if x == y:
    print("x is equal to y")    
# check if x is not equal to y
if x != y:
    print("x is not equal to y")    
# check if x is less than or equal to y
if x <= y:
    print("x is less than or equal to y")      
# check if x is greater than or equal to y
if x >= y:
    print("x is greater than or equal to y")    


#elif statement is a way to check multiple conditions in sequence.
a = int(input("What is the value of a? "))
# print what the user is y from user
b = int(input("What is the value of b? "))
# check if a is less than b
if a < b:
    print("a is less than b")
# check if a is greater than b
elif a > b:
    print("a is greater than b")    
# check if a is equal to b
elif a == b:
    print("a is equal to b")    
# check if a is not equal to b
elif a != b:
    print("a is not equal to b")    
# check if a is less than or equal to b
elif a <= b:
    print("a is less than or equal to b")      
# check if a is greater than or equal to b
elif a >= b:
    print("a is greater than or equal to b")   
# else statement is a way to execute a block of code if the specified condition is false. Catch all with any questions 
else:
    print("a and b is not a number")