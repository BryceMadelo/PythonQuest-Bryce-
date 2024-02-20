print("FACTORIAL CALCULATOR FOR ALF")
print("")

#Input
while True:
        nonNegative_integer = int(input("Please, enter a non-negative integer: "))
        if nonNegative_integer >= 0:
            break
        else:
            print("Invalid.")

#Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
#Output
output = factorial(nonNegative_integer)
print("")
print(f"The factorial of {nonNegative_integer} is {output}")