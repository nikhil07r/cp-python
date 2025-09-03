#print the pattern 
#1
#1*
#1*3
#1*3*
#1*3*5

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if j % 2 != 0:
            print(j, end="")
        else:
            print("*", end="")
    print()