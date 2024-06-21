#Approach : DP - Tabulation
# We define dp[i][j] to represent the number of paths to reach the grid(i,j)

# First, initialize all values in the first column and first row of dp
# then traverse other rows and columns, there are two cases:

# If obstacleGrid[i][j]==1, it means the number of paths 0 is so dp[i][j]=0
# If obstacleGrid[i][j]==0 then dp[i][j] = dp[i-1][j] + dp[i][j-1]
# Finally, return dp[m-1][n-1]

# The time complexity is O(mxn) and the space complexity is O(mxn).
# Here, m and n are the number of rows and columns of the grid, respectively.


#My-Approach

#Make DP Array Diagram for Vizualization

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m , n = len(obstacleGrid) , len(obstacleGrid[0])
        
        dp= [[0]*(n) for _ in range(m)]
        
        for r in range(m):
            if obstacleGrid[r][0]==1: #checking correpondingly with the obstacleGrid if obstacle no path
                break
            dp[r][0] = 1
        
        for c in range(n):
            if obstacleGrid[0][c]==1:
                break
            dp[0][c] = 1
            
        for r in range(1,m):
            for c in range(1,n):
                if obstacleGrid[r][c]==0:
                    dp[r][c] = dp[r-1][c]+dp[r][c-1]
        
        return dp[m-1][n-1]



#Competative Programming Approch
#Here we do not need to worry about to set first row & column value in answer dp inaccordance with the obstacle presence in obstaclegrid

class Solution:
    def uniquePathsWithObstacles(self,obstacleGrid):
        m , n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0]*(n+1) for _ in range(m+1)]

        # dp[1][1] = dp[0][1] + dp[1][0]
        # so, set either dp[0][1]=1, or set dp[1][0]=1

        dp[0][1] = 1

        for i in range(1,m+1):
            for j in range(1,n+1):
                if obstacleGrid[i-1][j-1] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                #else ,== 1 ,obstacle skip and leave as 0

        return dp[m][n]







