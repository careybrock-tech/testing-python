# write a hello function that prints "Hello, World!"
# define function create functions in python
def hello():
    print("Hello Welcome to Python World!")


# get user input 
name = input("What is your name? ").strip().title()
# print function
hello()
# print name
print("Hello, " + name)

# write a hello function that prints "Hello, World!"
# define function create functions in python
# passing a parameter to function to print name the argument can be any name i choose)
def hello1(anynameargument):
    print("Hello Welcome to Python World!" , anynameargument)
    # get user input 
name1 = input("What is your name user? ").strip().title()
# print function
hello1(name1)

# write a hello function that prints "Hello, World!"
# define function create functions in python
# passing a parameter to function to print name the argument can be any name i choose with default value
def hello2(to="World"):
    print("Hello Welcome to Python World!" , to)
    # get user input 
hello2()
name2 = input("What is your name? ").strip().title()
# print function
hello2(name2)