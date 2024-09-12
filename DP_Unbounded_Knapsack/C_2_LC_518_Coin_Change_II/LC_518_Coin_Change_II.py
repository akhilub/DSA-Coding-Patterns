# Dynamic Programming (Complete Knapsack)

'''
We define f[i][j] as the number of coin combinations to make up the amount j using the first i types of coins. 

                                 f(i,j)
                                /     \
                            skip      pick
                            /           \
                        f(i-1,j)     f(i,j) + f(i,j-coin[i])
'''
# The time complexity is O(m x n), and the space complexity is O(m x n). 
# where m and n are the number of types of coins and the total amount, respectively.


from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        m = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(m)]

        # Populate the amount = 0 columns, as we will always have one way to make 0 amount (by choosing nothing)
        for i in range(m):
            dp[i][0] = 1

        # Process all sub-arrays for all capacities
        for i in range(m):
            for t in range(1, amount + 1):
                # Exclude the coin
                dp[i][t] = dp[i - 1][t]
                # Include the coin, if it does not exceed the amount
                if t >= coins[i]:
                    dp[i][t] += dp[i][t - coins[i]]

        # Total combinations will be at the bottom-right corner
        print(dp)
        return dp[m-1][amount]     






'''Go with this approach in interviews'''
#Bottom Up DP - Tabulation

#Why Bottom Up?
#Because in the decision tree we are trying to find the topmost value (dp[n-1]) to reach their we start
#from bottom (dp[0]) and then traverse upward in the tree.

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
        return dp[-1] #dp[amount]

