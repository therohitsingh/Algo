def search(a,l,h,k):
    if l>h:
        return -1

    mid = (l+h)//2
    if(a[mid]==x):
        return mid
    elif(a[l]<=a[mid]):

        if(x>=a[l] and x<=a[mid]):
            return search(a,l,mid-1,x)
        return search(a,mid+1,h,x)

    if(x>=a[mid] and x<=a[h]):
        return search(a,l,mid+1,h,x)
    return search(a,l,mid-1,x)

a = [30, 40, 50, 10, 20]
x = 6
i = search(a,0,len(a)-1,x)
print(i)




