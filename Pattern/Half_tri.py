# *	* * * * 
# *	* * * 
# *	* * 
# *	* 
# *	* * * * * 
# *	* * * 
 
# *	* * * * 
# print this pattern using * take n = 5

n = 5

for i in range(n, 0, -1):
    print("*", end=" ")
    for j in range(i - 1):
        print("*", end=" ")
    print()


for i in range(n, 2, -2):
    print("*", end=" ")
    for j in range(i - 1):
        print("*", end=" ")
    print()


for i in range(n, 0, -1):
    print("*", end=" ")
    for j in range(i - 1):
        print("*", end=" ")
    print()
