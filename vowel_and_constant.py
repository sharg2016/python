n= str(input())
vowel=0
consonant=0
for i in range(len(n)):
    if(n[i]=='a'or n[i]=='A' or n[i]=='e'or n[i]=='E'or n[i]=='i'or n[i]=='I'or n[i]=='o'or n[i]=='O'or n[i]=='u'or n[i]=='U'):
        vowel += 1


    else:
        consonant += 1

print(vowel,end=" ")
print(consonant)
