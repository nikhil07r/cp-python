# given n and i check if ith bit is set or not .
def ith_bit(n, i):
    if (n & (1 << i)) != 0:
        return True
    else:
        return False
n = 5
i = 2
if ith_bit(n, i):
    print(f"The {i}th bit is set in {n}.")
else:
    print(f"The {i}th bit is not set in {n}.")
