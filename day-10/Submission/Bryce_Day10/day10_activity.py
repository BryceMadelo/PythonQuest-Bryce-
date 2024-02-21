import json

#Input
name = input("Enter your name: ")
age = input("Enter your age: ")
fav_food = input("Enter your favorite food: ")

#Dictionary
user_data = {
    "Name": name,
    "Age": age,
    "Favorite Food": fav_food
}

#Save to json file
try:
    with open("output.json", "w") as json_file:
        data = json.dumps(user_data, indent=2)
        json_file.write(data)
    print("User's data has been saved to 'output.json' file.")
except Exception as e:
    print(f"An error occurred: {e}")