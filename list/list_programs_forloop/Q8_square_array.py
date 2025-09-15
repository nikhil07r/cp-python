A = list(map(int, input("Enter numbers: ").split()))
squares = []
for x in A:
    squares.append(x*x)
print(squares)