def subsum(a,n,sum):
    if sum==0:
        return True
    if n==0 and sum!=0:
        return False    

    if a[n-1]>sum:
        return subsum(a,n-1,sum)
    return subsum(a,n-1,sum) or subsum(a,n-1,sum-a[n-1])        




def part(a,n):
    sum = 0
    for i in range(0,n):
        sum+=a[i]
    if sum % 2 != 0:
        return False
    return subsum(a,n,sum//2)    


