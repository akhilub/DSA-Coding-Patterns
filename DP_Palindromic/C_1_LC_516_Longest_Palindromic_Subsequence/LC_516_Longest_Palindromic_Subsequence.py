# We can bruteforce, but it takes ages. As the time complexity to generate all subsequence is O(2^N) i.e. C(n,0)+C(n,1)+C(n,2)+...+C(n,n)
# and it takes O(N) time to check if each subsequence is a palindrome. So overall time complexity of bruteforcing is O(N.2^N).


# LONGEST PALINDROMIC SUBSEQUENCE VIA TOP DOWN DYNAMIC PROGRAMMING ALGORITHM

# If we use dp[l][r] to denote the longest palindrome we can get at the substring s[l:r+1], then we know the following:

#             {   1  ,when l==r i.e any single character is a palindrome and 
# dp[l][r]  = {   0  ,where l is larger than r because it is invalid substring.
#             {   dp[l+1][r-1] + 2 , when s[l]==s[r] 
#             {   max(dp[l+1][r],dp[l][r-1])   ,otherwise (meaning when s[l]!=s[r])



# Using Recursion with Memoization, we can implement the Top-Down Dynamic Programming Algorithm:
# We use the @cache i.e. “@lru_cache(None)” or “@lru_cache(maxsize=None)” to cache the values aka memoziation. 
#Alternatively, we can use a dictionary or hash map to explicitly cache the values.

# The time complexity is O(N^2) as the left and right boundaries are range from 0 to N

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        n = len(s)
        @cache
        def dp(l,r):
            if l>r:
                return 0
            if l==r:
                return 1 
            if s[l]==s[r]:
                return 2 + dp(l+1,r-1)
            return max( dp(l+1,r) , dp(l,r-1))
            
        return dp(0,n-1)



#Using notebook Dictionary(Memoization)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        n = len(s)
        nb={}     # Memoization dictionary to store results of subproblems
        def dp(l,r):
            if l>r:
                return 0
            if l==r:
                return 1 
            if (l,r) in nb:
                return nb[(l,r)]
            if s[l]==s[r]:
                nb[(l,r)]=2 + dp(l+1,r-1)
            else:
                nb[(l,r)] = max(dp(l+1,r) , dp(l,r-1))
            return nb[(l,r)]
            
        return dp(0,n-1)


# COMPUTE THE LONGEST PALINDROMIC SUBSEQUENCE VIA BOTTOM-UP DYNAMIC PROGRAMMING ALGORITHM
# Starting from the bottom, we can compute the Two Dimensional DP array using iteration.
# The time complexity is O(N^2), and the space complexity is also O(N^2) as we are using the DP 2-D array to store the values.

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        n = len(s)

        dp = [[0]*n for _ in range(n)]

        for l in range(n-1,-1,-1):
            dp[l][l]=1
            for r in range(l+1,n):
                if s[l]==s[r]:                                   # case 1: elements at the beginning and the end are the same
                    dp[l][r] = 2 + dp[l+1][r-1]
                else:                                            # case 2: skip one element either from the beginning or the end
                    dp[l][r] = max(dp[l+1][r],dp[l][r-1])

        return dp[0][-1] # or dp[0][n-1]