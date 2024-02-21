try:
    with open("self-introduction.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("The file 'self-introduction.txt' can't be found.")
except Exception as e:
    print(f"An error occurred: {e}")
