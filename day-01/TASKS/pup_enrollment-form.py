print('PUP Enrollment Form')
#Data Input
full_name = input("Enter your full name: ")
age = input("Enter your age: ")
gwa = input("Enter your previous general weighted average: ")
is_cloudMember = input("Are you a member of AWS Cloud Club? (yes/no): ").lower() == "yes"

print("")
#Output
print("Your Enrollment Form")
print("Name: " + full_name)
print("Age: " + age)
print("GWA: " + gwa)
print("Awstraunot: ", is_cloudMember)