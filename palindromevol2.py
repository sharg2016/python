def palindorme(number):
    reverse = 0
    duplicate = number

    while number>0:
        remaind = number % 10
        reverse = reverse * 10 + remaind
        number  = number // 10

    if reverse==duplicate:
        return True

    else:
        return False





n= int(input())
if palindorme(n)==True:
    print(n)

else:
    while(palindorme(n)==False):
         rev=0
         r=n
         while n>0:
             a=n%10
             rev=rev*10+a

             n=n//10

         s=r+rev
         print(s)