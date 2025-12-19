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

# or you can use the if-else statement to check multiple conditions in sequence.
if x < y or x > y:
    print("x is not equal to y")

try:
    # elif statement is a way to check multiple conditions in sequence.
    a = int(input("What is the value of a? "))
    # print what the user is b from user
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
    # else statement is a catch-all for any other case
    else:
        print("Comparison complete")
except ValueError:
    print("That wasn't a number!")


score = int(input("Score:"))
if score >= 90 and score <= 100:
    print("Grade: A")       
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")


