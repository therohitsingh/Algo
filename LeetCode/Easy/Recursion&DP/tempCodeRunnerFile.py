def string(List):
    return "".join(List)

def permutate(l,r,a):
    if l==r:
        print(string(a))
    for i in range(l,r+1):
        a[l],a[i]=a[l],a[i]
        permutate(l+1,r,a)
        a[l],a[i]=a[l],a[i]
string = "ABC"
n = len(string)
a = list(string)
permutate(a,0,n-1)