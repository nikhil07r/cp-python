s = input()
words = s.split()
rev = [w[::-1] for w in words]
print(" ".join(rev))
