# Approach: Bottom Up DP
# Time:O(m*n)
# Space:O(m*n)


""" 
To solve this problem, we can use a bottom-up dynamic programming approach. We use a two-dimensional array, dp, to store the results of subproblems. 
The value dp[i][j] represents the length of the LCS between the first i elements of text1 and the first j elements of text2.
We create a two-dimensional array, dp, with dimensions (m + 1) x (n + 1). The “+1” is added to accommodate the base cases where either of the arrays is empty.

The nested loops iterate through the elements of text1 and text2. 
For each pair of elements, 
if they are equal, we increment the LCS length by 1 and store it in dp[i][j]. 
If they are not equal, we take the maximum LCS length obtained from the previous elements (either by excluding text1[i] or text2[j]) and store it in dp[i][j].


Finally, we returns the value stored in the bottom-right corner of the dp array, which represents the length of the LCS.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        # dp[i][j] := the length of LCS(text1[0..i), text2[0..j))
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[m][n]



#OR another way of writing , if we handle numbers from right to left

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        # dp[i][j] := the length of LCS(text1[0..i), text2[0..j))
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]













# Approach: Space Optimization Bottom Up DP
# Time:O(m*n)
# Space:O(n)


"""
The dp[i][j] is only dependent on dp[i-1][j] and dp[i][j-1] or dp[i-1][j-1], 

thus, we don’t need to store entire 2D DP Matrix, instead, we can use only two single arrays, one for the previous row e.g. dp[i-1], and one of the current row dp[i]. 
Then, we can optimise the DP solution to O(N) space where N is the less of N1 and N2 (the lengths for two arrays). The time complexity is O(N1*N2).

Each iteration, we set the current row to previous row via Deep Copy.
"""

from copy import deepcopy 


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        # only allocate a row of n (text2 size)
        dp = [0] * (n + 1)
        # new array of (text2 size) to Reset prev for each row
        dp_prev = deepcopy(dp) #[0] * (n + 1) 

        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[j + 1] = 1 + dp_prev[j]
                else:
                    dp[j + 1] = max(dp[j], dp_prev[j + 1])

            dp_prev = dp[:]    

        return dp[n]



class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        # only allocate a row of n (text2 size)
        dp = [0] * (n + 1)
        
        for i in range(m):
            prev = 0  # Reset prev for each row
            for j in range(n):
                cache = dp[j+1]  # Store current cell before overwriting
                if text1[i] == text2[j]:
                    dp[j + 1] = 1 + prev
                else:
                    dp[j + 1] = max(dp[j], cache)

                prev = cache # Update prev here, after using it

        return dp[n]




# Approach:Top Down DP (Recursion +Memoization)

'''
We define f[i][i] as the length of the longest common subsequence of the first i characters of text and the first j characters of text2. 

Therefore, the answer is f[m][n], where m and n are the lengths of text1 and text2, respectively.

If the `ith` character of text1 and the `jth` character of text2 are the same, then f[i][j] = f[i - 1][j - 1] + 1; 
if the `ith` character of text` and the `jth` character of text2 are different, then f[i][j] = max(f[i - 1][j], f[j - 1][i]).
Terminal cases : f(i,j) =0 , if i or j crosses the left boundary (i is smaller than zero, or j is smaller than zero).
  


The state transition equation is: 
        
            {       0                        , if i<0  or j<0
f[i][j] =   {  f[i - 1][j - 1] + 1 ,         , if text1[i]==text2[i]
            {  max(f[i - 1][j], f[j - 1][i]) , if text1[i]!=text2[i]


The time complexity is O(m x n), and the space complexity is O(m x n). Here, m and n are the lengths of text 1 and text2, respectively.


'''
from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m , n = len(text1) , len(text2)

        @cache
        def f(i,j):
            if i<0 or j<0:
                return 0 
            if text1[i]==text2[j]:
                return 1 + f(i-1,j-1)
            return max(f(i-1,j),f(i,j-1))
        return f(m-1,n-1)



#OR If we handle the numbers from left to the right, we have a similar DP approach.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m , n = len(text1) , len(text2)

        @cache
        def f(i,j):
            if i>m-1 or j>n-1:
                return 0 
            if text1[i]==text2[j]:
                return 1 + f(i+1,j+1)
            return max(f(i+1,j),f(i,j+1))
        return f(0,0)
