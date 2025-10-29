t = int(input())
vowels = "aeiouAEIOU"

for _ in range(t):
    s = input()
    v = c = 0
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                v += 1
            else:
                c += 1
    print(v, c)
