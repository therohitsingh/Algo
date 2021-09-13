def secondlargest(a,n):
    lar = 0
    seclar = 0
    for i in range(n):
        if a[i]>lar:
            lar = a[i]
    for i in range(n):
        if a[i]>seclar and a[i]!=lar:
            seclar = a[i]
    print(seclar)

a = [10, 20, 4, 45, 99]
n = len(a)
secondlargest(a,n)