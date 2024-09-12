#Greedy approach doesn’t work. For example, 23 is equal to 9 + 9 + 4 + 1 but if you go for greedy which to pick the largest square number less than N, then it will be equal to 16 + 4 + 1 + 1 + 1 which is not optimial.
#Mathematically proven, we need at most four perfect square numbers to sum up to a positive integer.



# TOP-DOWN DYNAMIC PROGRAMMING ALGORIHTM TO COMPUTE THE PERFECT SQUARES

'''
For example, we can use F(N) to represent the least number of perfect squares to sum up to N, then we can memorize it via Dynamic Programming process:

F(N) = min(F(N),F(N-j*j)) where j>=1 and j*j<=N
The base case is F(0)=0

Using the @cache keyword or @lru_cache(None) or @lru_cache(maxsize=None) as the Memoization Technique together with Recursion which virtually make it Top-Down Dynamic Programming Algorithm:
'''
class Solution:
    def numSquares(self,n):
        @cache
        def f(i):
            if i==0:
                return 0
            ans = math.inf
            j=1
            while j*j<=i:
                ans = min(ans,f(i-j*j)+1)
                j+=1
            return ans
        return f(n)


# Time complexity is O(N.Sqrt(N)).Space complexity is O(N).
# This is Top-Down process as we are computing the F(N) and then recursively computing smaller F(i) values where N-i is a perfect square.





# BOTTOM-UP DYNAMIC PROGRAMMING ALGORIHTM TO COMPUTE THE PERFECT SQUARES
# The Bottom-up Dynamic Programming computes F(0), and then F(1) and then F(2) until we reach the value of F(N). The process is bottom-up.

class Solution:
    def numSquares(self, n: int) -> int:
        # dp[i]:= to represent the least number of perfect square numbers that sum to i.
        dp = [float('inf')]*(n+1)
        dp[0] = 0 
        for i in range(1,n+1):
            j =1
            while j*j<=i:
                dp[i] = min(dp[i],dp[i-j*j]+1)
                j+=1
                
        return dp[n]

# We are using an DP array to store the F(i) values where i is from 0 to N inclusive. 
# The time complexity is same O(N.Sqrt(N)) and space complexity is O(N).