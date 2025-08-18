#print the reverse of a number using loop
n = int(input("Enter a number: "))
reverse = 0 
while n > 0:
    reverse = reverse * 10 +n % 10
    n //= 10
print("reverse of a number" , reverse)
