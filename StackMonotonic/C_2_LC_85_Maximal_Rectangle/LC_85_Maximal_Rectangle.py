#Approach:Monotonic Stack

# Time: O(mn)
# Space: O(n)

'''
We treat each row as the base of the histogram, and calculate the maximum area of the histogram for each row.

The time complexity is O(m×n), where m represents the number of rows in matrix, and 
n represents the number of columns in matrix.

'''

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:return 0
        
        heights = [0]*len(matrix[0])
        ans = 0
        for row in matrix:
            for j,V in enumerate(row):
                heights[j] = 0 if V==0 else heights[j]+1            #else case is for when V==1(i.e if V==1)
            
            ans = max(ans,self.largestRectangleArea(heights))
            
        return ans
    
    
    def largestRectangleArea(self,heights:List[int])->int:
        n = len(heights)
        left = [-1]*n 
        right = [n]*n 
        
        stk = []
        for i in range(n):
            h=heights[i]
            while stk and heights[stk[-1]]>=h:
                stk.pop()
            if stk:
                left = stk[-1]
            stk.append(i)            
        
        stk = []
        for i in range(n-1,-1,-1):
            h=heights[i]
            while stk and heights[stk[-1]]>=h:
                stk.pop()
            if stk:
                right = stk[-1]
            stk.append(i)
            
        return max(h*(right[i]-left[i]-1) for i ,h in enumerate(heights))         
        
        