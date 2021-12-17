def fact(a):
    mul=1
    for i in range(1,a+1):
        mul = mul*i

    return mul

def strong_number(n):
    d=n
    sum=0
    while n>0:
        r=n%10
        sum=sum+fact(r)
        n=n//10

    if(sum==d):
        return True

    else:
        return False


b=int(input())
for i in range(1,b+1):
    if strong_number(i):
        print(i,end=" ")
