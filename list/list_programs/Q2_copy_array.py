A = list(map(int, input("Enter numbers: ").split()))
B = int(input("Enter value of B: "))
print([x + B for x in A])