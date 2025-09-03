#power of a^b

a = 3
b =2 

a = int(input("Enter a number: "))
b = int(input("Enter the power: "))
power = 1
for i in range(b):
        power = power * a
print(power )