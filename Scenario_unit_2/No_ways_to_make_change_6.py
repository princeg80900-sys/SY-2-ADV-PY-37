coins = list(map(int, input("Enter coins: ").split()))
amount = int(input("Enter target amount: "))

dp = [0] * (amount + 1)

dp[0] = 1

for coin in coins:

    for i in range(coin, amount + 1):

        dp[i] = dp[i] + dp[i - coin]

print("Number of ways:", dp[amount])

#OUTPUT: 
#-------------------------
# Enter coins: 1 2 5
# Enter target amount: 5
# Number of ways: 4
#-------------------------
