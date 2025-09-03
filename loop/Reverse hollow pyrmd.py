n=int(input("enter the number of rows"))
for i in range(n,0,-1):
    for j in range(n-i+1):
        print("*",end="")
    for j in range(2*i-2):
       print(" ",end="")
    for j in range(n-i+1):
        print("*",end="")
    print()