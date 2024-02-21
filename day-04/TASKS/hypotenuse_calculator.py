import math

print("HYPOTENUSE CALCULATOR FOR ALF")
print("")

#Input Values
while True:
    try:
        sideA = float(input("Please, enter the length of side A: "))
        sideB = float(input("Please, enter the length of side B: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

#Output
hypotenuse = math.sqrt(sideA ** 2 + sideB ** 2)
print("")
print(f"The hypotenuse of the right-angled triangle is: {hypotenuse:.2f}")