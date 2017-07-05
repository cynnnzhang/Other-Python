
x1 = int(input("Enter the x value of your first coordinate: "))
y1 = int(input("Enter the y value of your first coordinate: "))
x2 = int(input("Enter the x value of your second coordinate: "))
y2 = int(input("Enter the y value of your second coordinate: "))

if y1 == y2:
    print("The line is horizontal")
    print("Its equation is x =", y1)

elif x1 == x2:
    print("The line is vertical")
    print("Its equation is y =", x1)

else:
    m = (y2 - y1)/(x2 - x1)
    b = y1 - m * x1

    print("The equation of the line in slope-intercept form is y =", m,"x","+",b)
