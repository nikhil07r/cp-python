# give an array you have given a string s and you have to find all amazing sub-string of s .an amazing substring is 1 that start with a vowel
s = "abec"
vowels = "aeiouAEIOU"
result = []

for i in range(len(s)):
    if s[i] in vowels:
        for j in range(i+1, len(s)+1):
            result.append(s[i:j])

print(result)