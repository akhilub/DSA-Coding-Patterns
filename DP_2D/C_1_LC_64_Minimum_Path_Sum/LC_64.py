#Approach : DP 
# We define f[i][j] to represent the minimum path sum from the top left corner to (i, j).
# Initially, f[0][0] = grid[0][0], and the answer is f[m - 1][n - 1].

# Consider f[i][j]:
# • If j=0,then f[i][j]= f[i-1][j]+grid[i][j]；
# • If i= 0, then f[i][j]= f[i][j-1]+grid[i][j]
# • Ifi>0andj> 0,then f[i][j] = min（f[i-1][j],f[i][j-1]）+grid[i][j].
# Finally, return f[m - 1]n - 1].
# The time complexity is O(m x n), and the space complexity is O(m x n). Here, m and n are the number of rows and columns of the grid,





class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        dp = [[0]*n for _ in range(m)]
        
        dp[0][0] = grid[0][0]
        
        for r in range(1,m):
            dp[r][0] = dp[r-1][0]+grid[r][0]
            
        for c in range(1,n):
            dp[0][c] = dp[0][c-1]+grid[0][c]
        
        
        for r in range(1,m):
            for c in range(1,n):
                dp[r][c] = min(dp[r-1][c],dp[r][c-1]) + grid[r][c]
                
                
        return dp[m-1][n-1]
                