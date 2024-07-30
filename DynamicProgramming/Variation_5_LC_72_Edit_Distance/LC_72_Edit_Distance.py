# We define  f[i][j] as the minimum number of operations to convert word1 of length i to word2 of length j. 

# f[i][0] = i , i∈[1,m]
# f[0][j] = j , j∈[0,n]

# We consider f[i][j]:

# If word1[i-1]=word2[j- 1], then we only need to consider the minimum number of operations to convert word1 of length `i-1` to word2 of length `j-1`, so 
# f[i][j]=f[i−1][j−1];

# Otherwise, we can consider insert, delete, and replace operations, then 
# f[i][j]=min(f[i−1][j],f[i][j−1],f[i−1][j−1])+1.


# Finally, we can get the state transition equation:

#          { i ,if j=0 
# f[i][j]= { j ,if i=0 
#          { f[i−1][j−1],​ if word1[i−1] = word2[j−1] 
#          { min(f[i−1][j],f[i][j−1],f[i−1][j−1])+1, otherwise​


# Finally, we return f[m][n].
# The time complexity is O(m×n), and the space complexity is O(m×n) where m and  n are the lengths of word1 and word2 respectively.


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        #Create dp
        dp = [[0]*(n+1) for _ in range(m+1)]
        #Intialize the first row and column

        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j

        #Fill up the dp array
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j] = 1+min(dp[i-1][j],            #Delete
                                    dp[i][j-1],             #Insert
                                    dp[i-1][j-1])           #Replace
         
        #Return the minimum no of operations            
        return dp[m][n]
