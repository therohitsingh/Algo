def trappingrain(a,n):

    res = 0

    for i in range(1,n-1):
        left = a[i]
        for j in range(i):
            left = max(left,a[j])

        right = a[i]

        for j in range(i+1):
            right = max(right,a[j])

        res = res+(min(left,right)-a[i])        