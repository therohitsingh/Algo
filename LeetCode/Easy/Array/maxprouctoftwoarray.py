def max(a,n):
 
    a.sort()
    return (a[n-1]-1)*(a[n-2]-1)

a=[3,4,5,2]
n =len(a)
print(max(a,n))   