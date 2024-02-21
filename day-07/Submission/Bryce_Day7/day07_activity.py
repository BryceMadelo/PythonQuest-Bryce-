#Input

name = input("Please, enter your name: ")

try:
    with open("user_info.txt", "w") as file:
        file.write(name) #writes name of user to txt file.
    print(f"your name '{name}' has been written to 'user_info.txt'.")
except Exception  as e:
    print(f"An error has occurred: {e}")