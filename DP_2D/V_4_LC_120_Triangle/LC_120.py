# BOTTOM-UP DYNAMIC PROGRAMMING ALGORITHM TO COMPUTE THE MINIMUM PATH SUM
# The minimum path sum is the same if you calculate it top to bottom, or bottom to top. Thus, the Dynamic Programming transistion function is:

# DP(r,c) = min(DP(r+1,c),DP(r+1,c+1)) + T(r,c)


#TC:O(N^2)
#SC:O(N^2)

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        # Initialize dp with the same dimensions as triangle
        dp = [[0]*len(row) for row in triangle]
        
        # Base case: the bottom row of dp is the same as the bottom row of triangle
        dp[-1] = triangle[-1]
        
        # Fill the dp array from bottom to top
        for r in range(len(triangle)-2,-1,-1):
            for c in range(len(triangle[r])):
                dp[r][c] = triangle[r][c]+ min(dp[r+1][c+1],dp[r+1][c])
                
        return dp[0][0]


#Follow up: Solution
#TC:O(N^2)
#SC:O(N)

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        # Initialize a dp array with the same length as the last row of the triangle
        dp[-1] =trinagle[-1][:]
        
        # Iterate from the second last row to the top row
        for r in range(len(triangle)-2,-1,-1):
            for c in range(len(triangle[r])):
                # Update dp[col] with the minimum path sum of the two possible moves
                dp[c] = triangle[r][c]+ min(dp[c+1],dp[c])
                
        return dp[0]


# Note:You can't initialize dp as dp = triangle[-1] directly because it creates a reference to the same list object as the last row of triangle. This means any modifications to dp will also modify triangle[-1], which is not desirable since you want dp to be an independent array that you can modify freely.

# To ensure dp is a separate list that can be modified without affecting triangle, you should create a copy of the last row of triangle. This can be done using list slicing, as shown here `dp = triangle[-1][:]`


# `dp = deepcopy(triangle[-1])`
# Using deepcopy from the copy module is another valid way to ensure that dp is a separate object from triangle[-1]. However, since the elements of triangle[-1] are integers (which are immutable in Python), a shallow copy created by dp = triangle[-1][:] or dp = triangle[-1][::] is sufficient. Using deepcopy is typically more useful when dealing with nested lists or mutable objects within the list.




#My Approach
#Use this in interviews
#TC:O(N^2)
#SC:O(1)

# We can overwrite the existing Triangle, from bottom-to-up, from left to right.
# The minimum path sum will then be at T[0][0]. The time complexity is O(RC) and the space complexity is O(1) as we are using the given Triangle to store the intermediate min path sum


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        # Fill the triangle array from bottom to top
        for r in range(m-2,-1,-1):
            for c in range(r+1):    # look c belongs to [0..len(triangle[r]] for every `r`
                triangle[r][c] = triangle[r][c]+ min(triangle[r+1][c+1],triangle[r+1][c])
                
        return triangle[0][0]