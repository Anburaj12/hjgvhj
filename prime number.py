a=input("enter the minimum value")
b=[]

for a in range(1,101):
    count=0
    for i in range(2,a//2+1):
        if(a%i==0):
            count=count+1
            break
    if(count==0 and a!=1):
        b.append(a)
print(b)
