# find the sum of a digits of a number using recursion.
def find_sum(n):
    if n == 0:
        return 0
    else:
        return n % 10 + find_sum(n // 10)