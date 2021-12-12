n=int(input())
li=[]
x=-100

for i in range(n):
    a=int(input())
    li.append(a)

j=sorted(list(set(li)))
print(j[-2])
