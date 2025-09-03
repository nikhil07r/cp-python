n = int(input("Enter a number: "))
print(f"\nTable of {n} is:")
for i in range(1, 11):
    temp = n * i
    print(f"{n} x {i} = {temp}")