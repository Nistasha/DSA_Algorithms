def climbingstairs(n):
    if n==0:
        return 1
    if n==1:
        return 1
    
    dp= [0] * (n+1)

    dp[0]=1
    dp[1]=1

    for i in range(2, n+1):
        dp[i]= dp[i-1]+ dp[i-2]

    return dp[n]

n= 5
print(f"to climb {n}th step we have {climbingstairs(n)} distinct ways")