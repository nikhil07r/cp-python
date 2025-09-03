# print this pattern
# *___*
# *___*
# *___*
# *___*

row = 4
col = 5
for i in range(row):
    for j in range(col):
        if j == 0 or j == col - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()