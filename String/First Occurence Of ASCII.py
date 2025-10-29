s = input()
b = int(input())
ch = chr(b)

if ch in s:
    print(s.index(ch))
else:
    print(-1)
