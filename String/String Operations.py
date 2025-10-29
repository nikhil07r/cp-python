s = input()
s = s + s          
s = ''.join(ch for ch in s if not ch.isupper()) 
vowels = "aeiou"
s = ''.join('#' if ch in vowels else ch for ch in s)
print(s)
