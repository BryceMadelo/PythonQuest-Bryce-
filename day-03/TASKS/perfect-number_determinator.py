print("PERFECT NUMBER DETERMINATOR FOR ALF")
print("")

#Input
while True:
        positive_integer = int(input("Please, enter a positive integer: "))
        if positive_integer >= 0:
            break
        else:
            print("Invalid.")
#Determinator
def isPerfect_number(n):
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

n = positive_integer

#Output 
if isPerfect_number(n):
    print("")
    print(f"{n} is a Perfect Number.")
else:
    print("")
    print(f"{n} is not a Perfect Number.")