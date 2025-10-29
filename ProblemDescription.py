def cslb(a, b):
    n = len(a)
    c = 0
    s = 0
    l = 0
    for r in range(n):
        s += a[r]
        while s >= b:
            s -= a[l]
            l += 1
        c += (r - l + 1)
    return c

a = [1, 2, 5, 6]
b = 10
res = cslb(a, b)
print(res)