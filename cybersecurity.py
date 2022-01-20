q= int(input())
l=[]

for j in range(q):
   n = input()
   l.append(n)
li=[]
c=[]
count=0


for i in l:

    p=""
    for k in i:
        e=ord(k)
        if e>=97 and e<=101:
            d=e+5
            p=p+chr(d)

        elif e>=102 and e<=106:
            d=e-5
            p=p+chr(d)
        elif e>=107 and e<=111:
            d=e+5
            p=p+chr(d)
        elif e >= 112 and e <= 116:
            d=e-5
            p=p+chr(d)
        else:
            p=p+k

    li.append(p)

for i in li:
    for k in i:
        if k in ['a','e','i','o','u']:
            count += 1

print(count)
print(li)

