n= str(input())
t= n.split(" ")
k=[]

for i in range(len(t)):
        r=t[i][::-1]
        k.append(r)

e=" ".join(k)
print(e)
