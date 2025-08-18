a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
if a<=0 or b<=0 or c <=0 or a+b+c != 180:
    print("Invalid angles for a triangle")
else:   
    largest = max(a, b, c)
    if largest == 90:
        print("right angle triangle")
    elif largest > 90:
        print("obtuse angle triangle")
    else:
        print(" acute angle triangle")