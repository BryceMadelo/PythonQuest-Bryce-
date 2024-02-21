print("PALINDROME CHECKER FOR ALF")
print("")

#Input
word = input("Please, enter a word/s to check: ")

#Palindrome Checker
reverse_word = word[::-1]

#Output
if word == reverse_word:
    print("")
    print(f"'{word.lower()}' is a palindrome.")
else:
    print("")
    print(f"'{word.lower()}' is not a palindrome.")