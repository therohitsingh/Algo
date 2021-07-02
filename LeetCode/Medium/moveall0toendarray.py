def zero(n,a):
    count = 0
    for i in range(0,n):
        if a[i]!=0:
            a[count]=a[i]
            count+=1
    while(count<n):
        a[count]=0
        count+=1

a = [1, 2, 0, 0, 0, 3, 6]
n = len(a)
zero(n,a)
print(a)