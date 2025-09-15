A = list(map(int, input("Enter numbers: ").split()))
mx = A[0]
mn = A[0]
for x in A:
    if x > mx:
        mx = x
    if x < mn:
        mn = x
print(mx, mn)