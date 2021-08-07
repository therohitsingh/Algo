def RightRotate(a, n, k):
 
    k = k % n
 
    for i in range(0, n):
 
        if(i < k):
 
            print(a[n + i - k], end = " ")
 
        else:
            print(a[i - k], end = " ");
 
    print("\n")
 
a = []
N = int(input())
for i in range(N):
    a.append(int(input()))
K = int(input())
     
RightRotate(a, N, K+1)
 