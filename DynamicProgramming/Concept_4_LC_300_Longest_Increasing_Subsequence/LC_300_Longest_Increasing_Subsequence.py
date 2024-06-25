# Bruteforcing takes O(2^N) to enumerate all subsequences and then we need O(N) time to check each subsequence, which amounts up to complexity O(N*2^N) which is not feasible to solve using the modern computers.

# BOTTOM-UP DYNAMIC PROGRAMMING ALGORITHM TO FIND THE LONGEST INCREASING SUBSEQUENCE

# We can use the Dynamic Programming Algorithm to Solve this problem in O(N^2) quadratic time. 
#Let F(N) be the number of the longest subsequence that ends nums[N], and the DP relation equation is:

# F(i) = max( F(i), F(j)+1 ) , if j < i and nums[j]<nums[i] 

# Initialize F(i) to 1 where i is [1, N].

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        # dp[i] the length of LIS ending in nums[i]
        dp = [1]*(n)
        for i in range(1,n):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)

        return max(dp)


# Since use a DP array and thus the space complexity is O(N).


# FINDING THE LONGEST INCREASING SUBSEQUENCE VIA TOP-DOWN DYNAMIC PROGRAMMING ALGORITHM
# We can do this via Recursion + Memoization aka Top-Down Dynamic Programming Algorithm. To compute F(N) value, we need to check the values between nums[0] to nums[N-1] and if it is smaller than nums[N], we recursively calling F function with a smaller value. But we have to use @cache (or @lru_cache(None), or @lru_cache(maxsize=None)) to rememebr the values that we already know so that we don’t re-calculate them over and over agin.

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        @cache
        def f(i):
            ans = 1
            for j in range(i):
                if nums[j]<nums[i]:
                    ans = max(ans, f(j)+1)
            return ans
        return max(f(i) for i in range(n))