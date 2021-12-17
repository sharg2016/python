n=int(input())
li=[]
lo=[]

sum=0

for i in range(n):
    b = int(input())
    li.append(b)

for i in range(n):
    
    
    while (li[i] > 0):
        r = li[i] % 10
        sum = sum + r
        li[i]= li[i]// 10
    
    
    d=sum
    sum=0
    lo.append(d)


    for i in range(n):
    print(lo[i])
