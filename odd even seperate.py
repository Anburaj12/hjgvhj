a=[3,6,7,8,9,2,1,5]
even=[]
odd=[]
for i in a:
    if (i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("even list",even)
print("odd list",odd)