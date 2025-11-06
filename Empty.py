# given an array A of length your task is to find maximum posible sum.of any non empty contigous subarray among of posible subarrays of A determine the one that hes the highest sum 
A = [2,5,6]
B = 10
n = len(A)
count = 0
for i in range(n):
    sum = 0
    for j in range(i, n):
        sum += A[j]
        if sum < B:
            count += 1
        else:
            break