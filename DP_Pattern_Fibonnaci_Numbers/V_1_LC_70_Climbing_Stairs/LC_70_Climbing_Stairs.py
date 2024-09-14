#Approach:DP
#Functional Relationalship
#If we use F(N) to represent the number of the ways to reach stair N, we know its previous possible locations could only be N-1 and N-2, and thus the Dynamic Programming Equation is:

'''
       { 1 ,i==1
f(i) = { 2, i==2
       {f(i-1)+f(i-2) , 2<i<=n i.e i == (2,n]
'''
#We can implement
#Top-Down DP (Recursion +Memoization)
#TC:O(n)
#SC:O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        def f(i,nb={}):
            if i==1:
                return 1
            if i==2:
                return 2
            if i in nb:
                return nb[i]
            nb[i] = f(i-1)+f(i-2)
            return nb[i]
        return f(n)




#Bottom-Up DP (Tablulation)
#TC:O(n)
#SC:O(n)

'''
To solve this problem, we can use dynamic programming. We'll build our solution from the bottom up.

For any step n, the number of ways to reach it is the sum of ways to reach (n-1) and (n-2). This is because we can reach step n by either taking one step from (n-1) or (n-2).

Note that the case where we take 2 steps from (n-2) to (n) is also included in this because we will have to take one step from (n-1) in this case.

The time complexity of this solution is O(n), where n is the number of steps.
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] := the number of ways to climb to the i-th stair
        dp = ['_', 1, 2] + [0] * (n - 1)
        for i in range(3, n + 1):
            dp[i] =  dp[i - 2] + dp[i-1]
        return dp[n]




#Bottom-up :No memory-DP (I prefer this)
'''We can use two variables to track only the previous two states.'''
#TC:O(n)
#SC:O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        #intial states f1(1st stair) and f2(2nd stair)
        f1 , f2 = 1 , 2
        for i in range(3,n+1): # i are the no of states to be computed
            fi = f1+f2
            f1 , f2 = f2 , fi
            
        return fi #note we intereseted in the ith state this time





#Greedy DP
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return b


