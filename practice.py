
n = int(input("Enter the number of rows for the hill pattern: "))

print("Invalid input. Please enter an integer.")


for i in range(1, n + 1):
    
   
    spacesm = " " * (n - i)
    
    stars = "*" * (2 * i - 1)
    
    print(spaces + stars)