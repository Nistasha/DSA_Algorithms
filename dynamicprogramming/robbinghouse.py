def robberhouse(money):
    if len(money) == 0:
        return 0
    if len(money) == 1:
        return money[0]

    #initialize dp array
    dp= [0] * len(money)

    #base cases
    dp[0] = money[0]
    dp[1]= max(money[0], money[1])

    #fill the dp array using the reccurence relation
    for i in range(2, len(money)):
        dp[i]= max(dp[i-1], money[i]+ dp[i-2])

    return dp[-1]

money= [2,7,9,3,1]
result= robberhouse(money)
print("Maximum money that can be robbed:", result)