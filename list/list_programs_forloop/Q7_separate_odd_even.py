A = list(map(int, input("Enter numbers: ").split()))
odds = []
evens = []
for x in A:
    if x % 2 == 0:
        evens.append(x)
    else:
        odds.append(x)
print(" ".join(map(str, odds)))
print(" ".join(map(str, evens)))