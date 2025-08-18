

# Q5. Read a number, check if it is divisible by 3 or its last digit is 4.

n = int(input("Enter n: "))
if n % 3 == 0 or n % 10 == 4:
    print("Divisible by 3 or its last digit is 4")
else:
    print("It is not divisible by 3 and its last digit is not 4")