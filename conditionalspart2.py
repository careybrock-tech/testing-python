
# match is like switch in other languages
# it is used to check if a value matches one of the cases

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
# the _ is a wildcard, it matches any value that doesn't match the previous cases