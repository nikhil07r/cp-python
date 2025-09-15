A = list(map(int, input("Enter numbers: ").split()))
even = sum(1 for x in A if x % 2 == 0)
odd = sum(1 for x in A if x % 2 != 0)
print(abs(even - odd))