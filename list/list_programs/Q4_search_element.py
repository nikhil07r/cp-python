A = list(map(int, input("Enter numbers: ").split()))
B = int(input("Enter number to search: "))
print(1 if B in A else 0)