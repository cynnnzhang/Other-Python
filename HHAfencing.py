#Introduction
print ("Welcome to Cynthia's incredible garden fencing homework helper!")
print ("This program will tell you how much it'll cost in total")
print ("to install a fence around your rectangular garden.")
print ("*" * 30)

#Input statements
length = float(input("Enter the length of your garden in feet: "))
width = float(input("Enter the width of your garden in feet: "))
costperFence = float(input("Enter the cost per foot of fencing found at your local hardware store:$ "))
labourCost = float(input("Enter the cost for labour/installation:$ "))
                   
#Calculations
perimeter =(length + width)*2
cost = (perimeter * costperFence)
roundedCost = round(perimeter * costperFence, 2)
totalCost = round(cost + labourCost, 2)
roundedPerimeter = round(perimeter, 2)

#Results
print ("*" * 30)
print ("Here are your results")
print ("*" * 30)

print ("The perimeter of your garden is", perimeter, "ft.")

print ("")

print ("Using the exact perimeter measurement...")
print ("The fencing will cost you","$", roundedCost)
print ("In total with labour/installation costs, it will cost you $", totalCost, "to install")
print ("fencing around your garden.")

