# given an n integer n count how many setbits in n .
def count_set_bits(n):
    if n == 0:
        return 0
    else:
        return (n & 1) + count_set_bits(n >> 1)