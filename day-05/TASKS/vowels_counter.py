print("VOWEL COUNTER FOR ALF")
print("")

#Input
while True:
    word = input("Please, enter a word/s to check: ")
    if word.isalpha():
        break
    else:
        print("")
        print("Please, enter letters only.")
        print("")

vowels_counter = 0
vowels = 'aeiou'

for letter in word.lower():
    if letter in vowels:
        vowels_counter += 1


#Output
print("")
print(f"The number of vowels in '{word}' is: {vowels_counter}")