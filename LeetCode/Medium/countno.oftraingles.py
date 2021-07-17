def traingle(a,n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if(a[i]+a[j]>a[k] and a[i]+a[k]>a[k] and a[j]+a[k]>a[i]):
                    count +=1
    return count 

a = [ 10, 21, 22, 100, 101, 200, 300 ]
n = len(a)
print(traingle(a,n))
             