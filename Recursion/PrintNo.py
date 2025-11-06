#using recursion print numbers 1 to n
def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n)

#using recursion print numbers n to 1
def print_numbers_reverse(n):
    if n == 0:
        return
    print(n)
    print_numbers_reverse(n - 1)
#using recursion find the nth fibonacci number
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)