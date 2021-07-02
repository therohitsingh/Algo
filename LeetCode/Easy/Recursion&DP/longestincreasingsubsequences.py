def lis(a,n):
    i,j,maxm = 0,0,0

    lst = [1 for s in range(n)]
    for i in range(n):
        for j in range(0,i):
            if a[i]>a[j] and lst[i]<lst[j]+1:
                lst[i] = lst[j]+1

        if maxm<lst[i]:

            maxm = lst[i]
    return maxm
a = [2 ,10 ,5 ,1 ,8 ,6 ,6 ,6 ,5]
n = len(a)
print("Length of lst is", lis(a, n))