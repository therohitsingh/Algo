from sys import maxint
def maxsub(a,size):
    maxf = -maxint-1
    maxe = 0
    for i in range(o,size):
        maxe+=arr[i]
        if(maxf<maxe):
            maxf = maxe
        if(maxe<0):
            maxe=0
    return maxf

a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7] 
print("Maximum contiguous sum is", maxsub(a,len(a)))