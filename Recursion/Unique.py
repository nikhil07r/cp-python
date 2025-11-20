# #Given N array elements, every element is repeated twice except one. Find that unique element.
def find_unique_element(arr):
    unique_element = 0
    for element in arr:
        unique_element ^= element
    return unique_element
arr = [2, 3, 5, 4, 5, 3, 4, 2, 6]
unique = find_unique_element(arr)
print("The unique element in the array is:", unique)


ans = 0
arr = [2, 3, 5, 4, 5, 3, 4, 2, 6]
for i in range(len(arr)):
    ans = ans ^ arr[i]
print(ans)