def pair(a,n):
    a.sort()

    s1 = a[0]*a[1]
    s2 = a[-1]*a[-2]

    if(s1<s2):
        print(a[-2],a[-1])
    else:
        print(a[0],a[1])    

a = [1, 4, 3, 6, 7, 0]
n = len(a)
pair(a, n)