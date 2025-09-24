n =int(input())
marks = list(map(int, input().split()))
passed = 0 
fail = 0
for i in marks :
    if i <= 35 :
        passed +=1
    else:
        fail +=1
print(passed , fail)        