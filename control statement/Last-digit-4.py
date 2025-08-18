# Q3. Check if its last digit is divisible by 4.

n = int(input("Enter n: "))
if (n % 10) % 4 == 0:
    print("divisible by 4")
else:
    print("not divisible by 4")
  