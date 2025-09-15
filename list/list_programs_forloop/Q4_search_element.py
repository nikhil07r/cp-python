A = list(map(int, input("Enter numbers: ").split()))
B = int(input("Enter number to search: "))
found = 0
for x in A:
    if x == B:
        found = 1
        break
print(found)