# given a list of integer and target a number find and print index of target number in the list . 
n = list(map(int, input("Enter the elements of array : ").split()))
t = int(input("Enter the target value : "))
for i in range(len(n)):
    if n[i] == t :
        print(i)
        break
else:
    print("Target not found")
    
