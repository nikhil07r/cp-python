# given an array and increment number generate a new array which contain all value of original array increase by increment value . 
n = list(map(int, input("Enter the elements of array : ").split()))
inc = int(input("Enter the increment value : "))
ans =[]
for i in n:
    ans.append(i+inc)
print(ans)

