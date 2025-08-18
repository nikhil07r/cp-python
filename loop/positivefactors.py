# print all factors/divisors of a +ve number using loop

n = int(input("Enter a positive number: "))
print("Factors of", n )    
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
        
