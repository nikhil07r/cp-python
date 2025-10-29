#given an array find the sum of all subarray sums using for loop.

# def sums(arr):
#     n = len(arr)
#     total= 0
#     for i in range(n):
#         array = arr[i] * (i + 1) * (n - i)
#         total += array
#     return total

# arr = [1, 2, 3]
# print(sums(arr))



#if we know how many subarray each element is coming we can solve this problem in O(n) time 

#in how many subarrays index 3 is coming
arr = [3, -2, 4, -1, 2, 6]
n = len(arr)
index = 3
count = (index + 1) * (n - index)
print(f"Element at index {index} ({arr[index]}) appears in {count} subarrays.")

