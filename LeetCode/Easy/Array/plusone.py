
a = [1,2,9]

b = []
c=0
for i in range(0,len(a)):
    if(a[i]==a[-1]):
        c=a[i]+1
        b.append(c)
    else:
        b.append(a[i])   
print(b)