n = int(input())
numbers = list(map(int, input().split()))
arr = []
for i in numbers:
    if i % 2 == 0:
        arr.append(i)
if len(arr) == 0:
    print(-1)        
else:
    for i in arr:
        print(i, end=" ")    