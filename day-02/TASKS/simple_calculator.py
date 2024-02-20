print("SIMPLE CALCULATOR FOR ALF")
print("")
#Enter Operand
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

#Enter Operator
operator = input("Enter the Operator (+, -, *, /): ")

#Result
output = 0

if operator == "+":
    output = first_number + second_number
elif operator == "-":
    output = first_number - second_number
elif operator == "*":
    output = first_number * second_number
elif operator == "/":

    if second_number != 0:
        output = first_number / second_number
    else:
        print("")
        print("Error: Division by zero is not allowed.")
        
else:
    print("Invalid operation.")

print("")
if operator in ["+", "-", "*"]:
    print("The result of ", first_number, operator, second_number, "is ", output)