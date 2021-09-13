def ratcount(a,r,u):
    n = len(a)
    if(n==0):
        return -1
    rat = r*u
    f = 0
    for i in range(n):
        f += a[i]
        if f>=rat:
            break
    if rat>f:
        return 0
    return i+1
r = int(input())
unit = int(input())
n = int(input())

arr = list(map(int,input().split()))
print(calculate(r,unit,arr,n))           

    


