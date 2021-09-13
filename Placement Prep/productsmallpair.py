#def ProductSmallestPair(sum, arr)

#The function accepts an integers sum and an 
# integer array arr of size n. Implement the 
# function to find the pair, 
# (arr[j], arr[k]) where j!=k, 
# Such that arr[j] and arr[k] are the least two elements of 
# array (arr[j] + arr[k] <= sum) and return the product of 
# element of this pair

def ProductSmallestPair(sum, a):
    n = len(a)
    for j in range(n):
        for k in range(j+1,n):
            if(a[j]+a[k]<=sum):
                print(a[j]*a[k]])
                break
            else:
                return 0    
n = int(input())
sum = int(input())
a = list(map(int,input().split()))


