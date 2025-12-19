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
def hello2(to="Default value"):
    print("Hello Welcome to Python World!" , to)
    # get user input 
hello2()
name2 = input("What is your name? ").strip().title()
# print function
hello2(name2)

# create a main function to run the program for hello
# organize my file
def main():
    name = input("What is your name? ").strip().title()
    hello(name)
def hello(to="World"):
    print("Hello, " + to)
# call the main function you have create this to call invoke the main function
main()

# create a main function to run the program for hello
# organize my file
def main2():
    name = input("What is your name? ").strip().title()
    hello(name)
# make sure to use the parameter in the function to print the name in scope of the function
def hello(name):
    print("Hello User, " , name)
# call the main function you have create this to call invoke the main function
main2()

