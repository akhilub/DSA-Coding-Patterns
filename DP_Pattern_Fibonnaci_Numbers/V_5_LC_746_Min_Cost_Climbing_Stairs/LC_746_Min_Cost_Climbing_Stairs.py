#Approach : Functional Relationship

#Algorithm : DP
'''
We define f(i) as the minimum cost required to reach the i-th step, 
Initially f(0) = f(1) = 0. The answer is f(n).

When i ≥ 2, we can directly reach the ith step from the (i - 1)th step using 1 step, or reach the ith step from the (i - 2)th step using 2 steps. Therefore, we have the state transition equation:
f(i) = min(f(i - 1) + cost[i - 1], f(i - 2) + cost[i - 2])
The final answer is f(n).
The time complexity is O(n), and the space complexity is O(n). Here, n is the length of the cost array.
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        @cache
        def f(i):
            if i==0:
                return 0
            if i==1:
                return 0
            return min(cost[i-1]+f(i-1), cost[i-2]+f(i-2))
        return f(n)





'''
#Top-Down DP
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        def f(i,nb={}):
            if i==0:
                return 0
            if i==1:
                return 0
            
            if i in nb:
                return nb[i]
            
            nb[i] = min(cost[i-1]+f(i-1), cost[i-2]+f(i-2))
            
            return nb[i]
            
        return f(n)
''' 









'''
# DP- Tabulation
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #Inital states
        n = len(cost)
        dp = [0,0]+[0]*(n-1)
        
        for i in range(2,n+1):
            dp[i] = min(cost[i-1]+dp[i-1],cost[i-2]+dp[i-2])
        
        return dp[n]
'''


# We notice that f(i) in the state transition equation is only related to f(i — 1) and f(i - 2)
# Therefore, we can use two variables f and g to alternately record the values of f(i - 2) and f(i - 1), which optimizes the space complexity to O(1).


#No-memory DP
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #Inital states
        n = len(cost)
        f0 , f1 = 0 , 0
        for i in range(2,n+1):
            fi = min(f1+cost[i-1], f0+cost[i-2])
            f0 , f1 = f1 , fi
        return fi 
