#Count Ways to N'th Stairs(Order does not matter)
def count(n):
    if(n==1 or n==2):
        return n
    for i in range(1,n):
        dp[i]=1
    for i in range(2,n):
        dp[i]=dp[i]+dp[i-2] 
    return dp[n]           