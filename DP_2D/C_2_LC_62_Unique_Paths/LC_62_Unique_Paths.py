#Approach : Top Down DP (Recursion + Memoization)

#m - no of rows
#n - no of cols
class Solution:
    def uniquePaths(self, m, n):
        def f(i , j , nb = {}):
            #terminal/base case
            if i == 0 or j ==0:
                return 1
            #if previous computed value in notebook give me that
            if (i,j) in nb:
                return nb[(i,j)]

            nb[(i,j)] = f(i-1,j) + f(i,j-1)

            return f(i-1,j) + f(i,j-1)

        return f(m-1,n-1)




#My-Approach : Bottom-Up DP (Tabulation)
class Solution:
    def uniquePaths(self,m,n):
        dp= [[0]*n for _ in range(m)] # m lists each list is of `size n`.

        for r in range(m):
            dp[r][0] = 1
        
        for c in range(n):
            dp[0][c] = 1

        for r in range(1,m):
            for c in range(1,n):
                dp[r][c] = dp[r-1][c]+ dp[r][c-1]

        return dp[m-1][n-1]




#Competative Programming Approach
'''
We define f[i][j] to represent the number of paths from the top left corner to (i,j)
initially f[0][0] =1 and the answer is f[m-1][n-1]

Consider f[i][j]
If i> 0 then f[i][j] can be reached by taking one step from f[i-1][j],
so f[i][j] = f[i][j] + f[i-1][j]

If j >0 then f[i][j] can be reached by taking one step from f[i][j-1],
so f[i][j] = f[i][j] + f[i][j-1]

Therefore, we have the following state transition equation:
                    { 1  , i =0 ,j =0
          f[i][j] = { f[i-1][j] + f[i][j-1] , otherwise
The final answer is f[m-1][n-1]


The time complexity is O(mxn) and the space complexity is O(mxn)
Here m and n are the number of rows and columns of the grid, respectively.


We notice that f[i][j] is only related to f[i-1][j] and f[i][j-1]
so we can optimize the first dimension space and only keep the second dimension space, resulting in a time complexity of 
O(mxn) and a space complexity of O(n)
'''

class Solution:
    def uniquePaths(m,n):
        # avoid setting dp[][] to 1 for i==0 or j==0 as initialization
        dp = [[1]*n for _ in range(m)]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
    
    
    
    
    





























#Mathematically Way C(m+n-2,m-1) = C(m+n-2,n-1)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # '//' -> is integer/floor division operation which gives quotient(integer number) of division  
        return self.fact(m+n-2)//(self.fact(m-1) * self.fact(n-1))
    
    def fact(self,N):
        def f(i,nb={}):
            if i ==0 or i==1:
                return 1
            if i in nb:
                return nb
            nb[i] = i*f(i-1)
            return nb[i]
        return f(N)



#Same above Pythonic Maths way
from math import comb
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m+n-2,m-1)
    
    
#factorial Exist in python3
from math import factorial
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return factorial(m+n-2)// (factorial(m-1)*factorial(n-1))
        