'''
To solve this problem, we'll use dynamic programming. We'll create a 2D array dp where dp[i][j] represents the side length of the largest square ending at position (i, j).

For each cell, if it's '1', we'll check the squares to its left, top, and top-left. The largest square ending at the current cell will be the minimum of these three squares plus 1.

We'll keep track of the maximum square side length as we go. The area of this maximum square will be our answer i.e maximum value among all dp[i][j].

The state transition equation is:



           { 0                                     , if matrix[i][j]== '0' 
dp[i][j] = { 1+min(dp[i-1][j],dp[i][j-1],dp[i][j]) , if matrix[i][j]== '1'
            

The time complexity of this solution is O(m*n), where m and n are the dimensions of the matrix.
'''







#Appraoch: 2D DP
#TC:O(m*n)
#SC:O(m*n)

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m , n = len(matrix),len(matrix[0])
        dp = [[0]*(n) for _ in range(m)]
        mx =0                               #mx - maximum length of sqaure
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='1':
                    #Check left,top and top-left corners
                    dp[i][j] = 1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                    mx = max(mx,dp[i][j])
        
        #Return the area of largest square            
        return mx*mx
    
    

















































#Approach:Optimized 1D DP
#TC:O(m*n)
#SC:O(n)  
    
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [0] * (n + 1)  # Use n+1 to avoid index out-of-bound issues
        mx = 0
        prev = 0  # This represents dp[j-1] from the previous row

        for i in range(m):
            for j in range(1, n + 1):  # Start from 1 because dp[j-1] requires this shift
                cache = dp[j]
                if matrix[i][j - 1] == '1':
                    dp[j] = 1 + min(dp[j], dp[j - 1], prev)
                else:
                    dp[j] = 0
                mx = max(mx, dp[j])
                prev = cache  # Update prev to the current dp[j]
        
        return mx * mx