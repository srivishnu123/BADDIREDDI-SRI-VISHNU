n=[1,2,8,9,12,46,76,82,15,20,30]
a={}
for i in range(1,10): 
    c=0
    for j in n:
        if j%i==0:
            c+=1
    a[i]=c
print(a)

