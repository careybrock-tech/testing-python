# operations on numbers are performed using arithmetic operators
# symbols used for arithmetic operations are +, -, *, /, %, **, //
# get user input for the number to add 
x = input("What is x: ")
# get user input for the number to add 
y = input("What is y: ")

# create a variable to hold the sum of x and y 
z1 = int(x) + int(y)

# print the sum of x and y 
print(z1)

# get user input for the number to add nest function

x = int(input("What is x: "))
# get user input for the number to add 
y = int(input("What is y: "))
# create a variable to hold the sum of x and y 
z = x + y
# print the sum of x and y 
print(z)

a = int(input("What is a: "))
# get user input for the number to add 
b  = int(input("What is b: "))
# print the sum of x and y 
print(a + b)

# a float is a number with a decimal point
# get user input for the number to add  
c = float(input("What is c: "))
# get user input for the number to add
d = float(input("What is d: "))
# create a variable to hold the sum of x and y 
e = c + d   
# print the sum of x and y  
print(e)

# a float is a number with a decimal point
# get user input for the number to add  
f = float(input("What is f: "))
# get user input for the number to add
g = float(input("What is g: "))
# create a variable to hold the sum of x and y 
h = f / g   
# print the sum of x and y  
print(h)

# a float is a number with a decimal point
# get user input for the number to add  
i = float(input("What is i: "))
# get user input for the number to add
j = float(input("What is j: "))
# create a variable to hold the sum of x and y  using th round function
k = round(i / j,2)   
# print the sum of x and y  
print(k)

# a float is a number with a decimal point
# get user input for the number to add  
l = float(input("What is l: "))
# get user input for the number to add
m = float(input("What is m: "))
# create a variable to hold the sum of x and y  using th round function
n = round(l / m,2)   
# print the sum of x and y  
#2f"{ is a sum of x and y is {n}")
print(f"{n:.2f}")

#  square the number in the function
def main3():
    x = int(input("What is x? "))
    print("x squared is", square(x))
def square(n):
    # return the square of n
    #######################
    # return n ** 2
    # return pow(n, 2)
    return n * n

main3()