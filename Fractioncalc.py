N1 = int(input("Enter 1st numerator: "))
D1 = int(input("Enter 1st denominator: "))
N2 = int(input("Enter 2nd numerator: "))
D2 = int(input("Enter 2nd denominator: "))
C = int(input("Enter common denominator: "))

A = (C/D1)*N1
B = (C/D2)*N2
N3 = A + B

print("The sum of the fractions is", N3, "/", C)
