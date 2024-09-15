'''
The Greedy Algorithm may not work here. 
For example, given coins [1, 20, 25], and the target is 60, if we greedily pick the most largest coin , 
we will end up with (25, 25, and 10 times of 1) i.e. 12 coins while the optimal solution will be 3 times 20 i.e. 3 coins.
'''


'''
This problem is like a unbounded knapsack problem, where we can use as many coins of the one type as we want. 
We can solve this via Depth First Search (Backtracking), and also we can solve this more efficiently using Dynamic Programming Algorithms.
In particular, the DP can be classified into Top-Down or Bottom-up.
'''



#DYNAMIC PROGRAMMING ALGORITHMS TO MAKE CHANGE
#Both DP algorithms have O(N) time and O(N) space.

'''
Let f(n) be the no of minimum coins to come up with the target n amount

Using Dynamic Programming Algorithm - we know the DP transition function:

f(n) = { min( f(n), f(n - coin) + 1 ) , for coin in [...coins...], if f(n - coin) is reachable
f(0) = 0
'''

#The Top Down DP (implemented via Recursion with Memoization aka @cache) is:

class Solution:
     def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def f(n):
            if n==0:
                return 0
            if n < 0:
                return math.inf # some large number greater than amount
            
            ans = math.inf 
            for j in range(len(coins)):
                ans = min(ans,f(n-coins[j]) + 1)

            return ans

        return -1 if f(amount)==math.inf else f(amount)

# In Top Down DP, we have to enlarge the recursion limit via sys.setrecursionlimit (to verify using sys.getrecursionlimit).



#Bottom Up DP (Tabulation)
'''
We maintain a one-dimensional dynamic array dp, where dp[i] represents the change of the smallest number of coins when the amount of money is i. 
Note that since the array starts from 0, one more bit must be applied. The size of the array is amount +1, so the final result can be saved in dp [amount].

Initialize dp[0] = 0, because if the target value is 0, no coins are needed. 

Other values can be initialized as amount+1, why? 
Because the smallest coin is 1, so amount requires at most amount coins, and amount+1 is equivalent to the current maximum.
• Note that the integer maximum value cannot be used for initialization here, because there is an operation of adding 1 to the subsequent state transition equation, which may cause overflow.

The next step is to find the state transition equation. 

Example 1, suppose I take a coin with a value of 5, then since the target value is 11, so if we know dp[6], then we know the dp of 11 Worth it?
So the way to update dp[i] is to traverse each coin. If the value of the traversed coin is less than the value of i (for example, a coin with a value of 5 cannot be used to update dp[3]), use dp[i-coins[j ]] + 1 to update dpLi], 

so the state transition equation is:  dp[i] = min(dp[i], dp[i-coins[j]] + 1);
among them
• coins[j] is the j-th coin
• i-coins[j] is the amount of money i minus the value of one of the coins, the remaining amount of money is found in the dp array

Then add 1 and compare the value in the current dp array, and update the dp array with the smaller one.
'''

class Solution:
    def coinChange(self,coins,amount):
        # dp[i] := the minimum number Of coins to make up i
        dp = [float('inf')]* (amount+1)             #instead of [float('inf')] we can also use [amount+1]
        dp[0] = 0
        
        for i in range(1,amount+1):                 #here i is integer amount from 1 till amount
            for c in coins:
                if i>=c and dp[i-c]!=float('inf'):
                    dp[i] = min(dp[i],dp[i-c]+1)

        return dp[amount] if dp[amount]!=float('inf') else -1










































'''Write this in interviews'''
#Approach 3: Traversing using coins first

#TC:O(mxn)
#SC:O(n) 
# where m and n are the number of types of coins and the total amount, respectively.

class Solution:
  def coinChange(self, coins: list[int], amount: int) -> int:
    # dp[i] := the minimum number Of coins to make up i
    dp = [amount + 1] * (amount+1)                      #[amount+1]  or [inf]
    dp[0] = 0 
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return -1 if dp[amount] == amount + 1 else dp[amount]  #amount +1   or inf
   


'''
return -1 if dp[amount] == amount + 1 else dp[amount]
                    ||
                    ||
return -1 if dp[-1] > amount else dp[-1]
                    ||
                    ||
return -1 if dp[-1] >= amount+1 else dp[-1]                   

'''



'''
dp = [amount + 1] * (amount+1)
dp[0] = 0
            ||
            ||
dp = [0]+[amount + 1] * (amount)

'''


   

#? Note:  `? - No ternary operator in Python3`
 


