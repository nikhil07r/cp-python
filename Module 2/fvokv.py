# find the no of occurance bob in string a consistinng of lower case letters .
a = "abcbobdbob"
count = 0  
for i in range(len(a) - 2):
    if a[i:i+3] == "bob":
        count += 1
print("Number of times bob occurs is:", count)
