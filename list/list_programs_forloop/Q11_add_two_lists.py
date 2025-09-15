A1 = list(map(int, input("Enter list1: ").split()))
A2 = list(map(int, input("Enter list2: ").split()))
result = []
for i in range(len(A1)):
    result.append(A1[i] + A2[i])
print(result)