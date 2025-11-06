# sum of N natural numbers using for loop .
# make an assumption 
# decide what your function does and trust it will it
# main logic solve bigger problem using breaking it down into smaller problems
# when a recursion stops

#
#def natural_numbers(n):
 #   total_sum = 0
#   
 #   for i in range(1, n + 1):
 #       total_sum += i
 #   return total_sum


# factorial of a number using recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# fibonacci series using recursion
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)