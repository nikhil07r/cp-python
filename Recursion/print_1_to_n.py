def print_up(n):
    if n == 0:
        return
    print_up(n-1)
    print(n, end=' ')

print_up(5)