n = int(input("enter a no."))
li = []
d = 0
x=-100
for i in range(n):
    a = int(input("enter numbers"))
    li.append(a)

for i in range(n):
    if d<li[i]:
        d=li[i]

for i in range(n):
    if x<li[i] and li[i]<d:
        x=li[i]




print(x)