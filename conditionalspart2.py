

# name1 if statement is used to check if a condition is true
# it is used to execute a block of code if the condition is true
name1 = input("What is your name ? ")
if name1 == "Harry":
    print("Gryffindor") 
elif name1 == "Hermione":    
    print("Gryffindor") 
elif name1 == "Ron":    
    print("Gryffindor") 
elif name1 == "Draco":
    print("Slytherin")
else:
    print("Who?")   

# match is like switch in other languages
# it is used to check if a value matches one of the cases
name = input("What is your name ? ")
match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

# name 2 uses or to check if a value is in a list
# it is used to execute a block of code if the value is in the list
name2 = input("What is your name ? ")
if name2 == "Harry" or name2 == "Hermione" or name2 == "Ron":
    print("Gryffindor")
elif name2 == "Draco":
    print("Slytherin")
else:
    print("Who is He or Her?")