#print the pattern of stars in a single line verticqlly and horizontally
n = int(input("enter number: "))
m = int(input("enter your number: "))
for i in range(n):
    for j in range(m):
        print("*", end="")
    print()  