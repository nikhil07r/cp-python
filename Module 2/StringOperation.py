A = "aeiOUz"

A = A + A   


small = ""
for ch in A:
    if ch.islower():     
        small += ch


final = ""
for ch in small:
    if ch in "aeiou":
        final += "#"
    else:
        final += ch

print(final)
