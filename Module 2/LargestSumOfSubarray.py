# given an interger array , find the subarray with the largest sum.example:-2,1,-3,4,-1,2,1,-5,4]
def subarray(arr):
    max_sum = arr[0]
    sum = arr[0]
    for num in arr[1:]:
        sum = max(num, sum + num)
        sum = max(max_sum, sum)
    return max_sum
array = [-2,1,-3,4,-1,2,1,-5,4]
result = subarray(array)
print("Maximum subarray sum:", result)  
