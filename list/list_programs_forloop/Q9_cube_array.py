A = list(map(int, input("Enter numbers: ").split()))
cubes = []
for x in A:
    cubes.append(x*x*x)
print(cubes)