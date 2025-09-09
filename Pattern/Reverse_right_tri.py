# print the reverse right angle triangle using * take n = 5

n = 5
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print() 