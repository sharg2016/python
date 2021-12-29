n=int(input())
d=str(n)
suml=0
sumr=0

if(len(d)%2==1):
    mid=len(d)//2

for i in range(0,mid):
    suml=suml+int(d[i])

for j in range(mid+1,len(d)):
    sumr=sumr+int(d[j])

if(suml==sumr):
    print(1)

else:
    print(0)
