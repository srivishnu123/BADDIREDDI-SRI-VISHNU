a=int(input())
if a%2==0:
    c=a-1
else:
    c=a
b=[]
d=1
e=0
while e<c:
    b.append(d)
    d+=2
    e+=1
print(b)

