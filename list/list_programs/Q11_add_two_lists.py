A1 = list(map(int, input("Enter list1: ").split()))
A2 = list(map(int, input("Enter list2: ").split()))
print([A1[i] + A2[i] for i in range(len(A1))])