# *	* * * * 
# *	* 
# *	* 
# *	* * * * * * 

# print the one side pattern and one in between using * take n = 5

n = 4
for i in range(n):
    if i == 0 or i == n - 1:
        print("*", end=" ")
        print("* " * (n - 1), end="")
        if i == n - 1:
            print("* " * (n - 2), end="")
    else:
        print("*", end=" ")
        print("*")
    print()
