A = list(map(int, input("Enter numbers: ").split()))
print(" ".join(map(str, [x for x in A if x % 2 != 0])))
print(" ".join(map(str, [x for x in A if x % 2 == 0])))