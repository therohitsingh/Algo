def inversion(a,n):
    in_count=0
    for i in range(n):
        for j in range(i+1,n):
            if a[i]>a[j]:
                in_count+=1
    return in_count

a = [1,20,6,4,5]
n = len(a)
print(inversion(a,n))