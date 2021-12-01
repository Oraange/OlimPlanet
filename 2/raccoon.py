n = int(input())

def get_raccoon(n):
    dp = [2,4]

    if n==0:
        return 2
    
    if n==1:
        return 4

    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])

    return dp[-1]

print(get_raccoon(n))