#print the pattern
#*______*
#*_____*
#*____*
#*___*
#*_*

rows = 5
for i in range(rows, 0, -1):
    for j in range(1, rows + 2 - i):
        if j == 1 or j == rows + 1 - i:
            print("*", end="")
        else:
            print("_", end="")
    print() 