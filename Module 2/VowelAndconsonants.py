a=int(input("No of Strings :"))
l=[]
for i in range(a):
    s=input("Enter String :")
    vowel=0
    consonent=0
    for j in range(len(s)):
        if s[j].isalpha():
            if s[j] in ('a','e','i','o','u','A','E','I','O','U'):
                vowel+=1
            else:
                consonent+=1
    l.append(vowel)
    l.append(consonent)
for i in range(0,len(l),2):
    print(l[i],l[i+1])

