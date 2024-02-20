print("BMI CALCULATOR FOR ALF")
print("")

#Inputs
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter you height in meters: "))

#Output
bmi = weight/(height**2)

#Classification
if bmi < 18.5:
    nutritional_status = "UNDERWEIGHT"
elif 18.5 <= bmi <= 24.9: 
    nutritional_status = "NORMAL WEIGHT"
elif 25.0 <= bmi <= 29.9:
    nutritional_status = "OVERWEIGHT"
elif bmi >= 30.0:
    nutritional_status = "OBESITY"

print("")
print("HEIGHT: ", height," - WEIGHT", weight)
print(f"BMI: {bmi:.2f} - NUTRITONAL STATUS: {nutritional_status}")