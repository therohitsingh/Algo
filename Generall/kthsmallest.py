def ksmall(n):
    arr.sort()
    return arr[k-1]

if __name__ == "__main__":
    arr = [12,3,5,7,19]
    n = len(arr)
    k = 2 
    print("kth smallest element",ksmall(arr,n,k))