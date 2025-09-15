A = list(map(int, input("Enter numbers: ").split()))
B = int(input("Enter value of B: "))
new_arr = []
for x in A:
    new_arr.append(x + B)
print(new_arr)