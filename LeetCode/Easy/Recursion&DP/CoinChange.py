def coinchange(S,m,n):
    if(n==0):
        return 1
    if (n<=0):
        return 0
    if(m<=0 and n>=1):
        return 0

    return coinchange(S,m-1,n) + coinchange(S,m,n-S[m-1])

a = [1,2,3]
m = len(a)
print(coinchange(a,m,4))

class Solution:
    def count(self, S, m, n): 
        # code here 
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if j >= S[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-S[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n,m = list(map(int, input().strip().split()))
        S = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(S,m,n))
# } Driver Code Ends