# Q4. Check if it's divisible by 3 and its last digit is 4.

n = int(input("\nEnter n: "))
if n % 3 == 0 and n % 10 == 4:
    print("\nDivisible by 3 and its last digit is 4")
else:
    print("\nIt is not divisible by 3 and last digit is not 4")