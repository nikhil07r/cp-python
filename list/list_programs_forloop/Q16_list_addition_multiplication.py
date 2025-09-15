l1 = [1, 2, 3, 5, 8, 9]
l2 = [3, 4, 5, 6, 7, 10]
result = []
for i in l1:
    result.append(i)
for i in l2:
    result.append(i)
print(result)

result1 = []
for _ in range(3):
    for i in l1:
        result1.append(i)
print(result1)