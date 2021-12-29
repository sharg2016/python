 def factorial(n):
    d=1
    for i in range(1,n+1):
        d= d*i

    return d

n= int(input())
f=n
sum=0
while n>0:
    r=n%10
    sum=sum+factorial(r)
    n=n//10

if(sum==f):
    print("yes")

else:
    print("no")
