import math

print("CYLINDER VOLUME CALCULATOR FOR ALF")
print("")

#Input Values
while True:
    try:
        r = float(input("Please, enter the radius of the cylinder: "))
        h = float(input("Please, enter the height of the cylinder: "))
        
        if r <= 0 or h <= 0:
            print("")
            print("Please, enter valid values of radius and height.")
            print("")
        else:
            break   
    except ValueError:
        print("")
        print("Invalid input. Please enter a valid number.")
        print("")

#Output
volume = math.pi * r ** 2 * h
print("")
print(f"The hypotenuse of the right-angled triangle is: {volume:.2f}")