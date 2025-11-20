# find the sum of a digits of a number using recursion.
def find_sum(n):
    if n == 0:
        return 0
    else:
        return n % 10 + find_sum(n // 10)
    
# write a recursive function for print the reverse of a string.
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])