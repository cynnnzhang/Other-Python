print("Welcome to Landmark Cinemas!")
print("*"*30)
age = int(input("Enter your age: "))

if age >= 65:
    threed = input("Is the movie you wish to see in 3-D?")
    
    if threed == "yes":
        print("Great! You're ticket will cost you $11.99")
    else:
        print("Great! You're ticket will cost you $8.99")

elif age >= 14:
    threed = input("Is the movie you wish to see in 3-D?")
    
    if threed == "yes":
        print("Great! You're ticket will cost you $15.99")
    else:
        print("Great! You're ticket will cost you $12.99")

elif age >= 3:
    threed = input("Is the movie you wish to see in 3-D?")
    
    if threed == "yes":
        print("Great! You're ticket will cost you $11.99")
    else:
        print("Great! You're ticket will cost you $8.99")
        
else:
    print("Sorry, kids under 3 are not allowed into the theatre")
