# print the sum of every single element in an array using def funcion.
def sum_of_array(arr):
    total = 0
    for num in arr:
        total += num
    return total
array = [1, 2, 3, 4, 5]
result = sum_of_array(array)
print("Sum of array elements:", result)