# *	* * * * 
# *	* * * 
# *	* * 
# *	* 
# *	* * * * * * * * * * * * * * 


# print this pattern using * take n = 5

n = 5
for i in range(n):
    print("*", end=" ")
    for j in range(n - i):
        print("*", end=" ")
    print()
if i == n - 1:
    for k in range(n * n):
        print("*", end=" ")
    print()