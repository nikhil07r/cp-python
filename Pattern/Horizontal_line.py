# *	* * * * * * * * * 
# *	* * * * 

# print this pattern using * take n = 5

rows = [8,4]   

for r in rows:
    print("*", end="")
    for i in range(r):
        print("*", end=" ")
    print()
