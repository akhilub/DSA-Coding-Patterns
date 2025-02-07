#Approach:Monotonic Stack (Increasing)
# Time: O(n)
# Space: O(n)

'''
We can enumerate the height `h` of each bar as the height of the rectangle. 
Using a monotonic stack, we find the index left[i], right[i] of the first bar with a height less than `h`
to the left and right. 
The area of the rectangle at this time is h x (right[i] - left[i] - 1). 
We can find the maximum value.

The time complexity is O(n), and the space complexity is O(n). 
Here, n represents the length of heights.
'''

#Use the monotonic stack template

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        left = [-1] * n
        right = [n] * n
        
        stk = []                                    # create an empty stack
        for i in range(n):                          # for each element in the array:
            h = heights[i]                          # current height
            while stk and heights[stk[-1]] >= h:    # while stack is not empty AND top of stack is more than the current element
                stk.pop()                           # pop the stack
            if stk:
                left[i] = stk[-1]
            stk.append(i)                           # push the current element to stack
        
        
        stk = []
        for i in range(n - 1, -1, -1):
            h = heights[i]
            while stk and heights[stk[-1]] >= h:
                stk.pop()
            if stk:
                right[i] = stk[-1]
            stk.append(i)
        
        return max(h * (right[i] - left[i] - 1) for i, h in enumerate(heights))












































































#Approach:Monotonic Stack(Decreasing)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #pair:(startIndex,height)
        
        for i , h in enumerate(heights):
            startIndex = i
            while stack and stack[-1][1] > h: # stack is not empty and top element in stack has a height less than the current height
                index,height = stack.pop()  # pop the top elements from the top of stack to check if this height could be the maxArea of the rectangle
                maxArea = max(maxArea,height*(i-index)) #width = currentIndex - index at which this height started i.e popped element index
                startIndex = index # Extend the startIndex all the way backward to the index that we just popped
            stack.append((startIndex,h))
        
        #Extend the enteries left in stack to all the way to the end of histogram
        for i, h in stack:
            maxArea = max(maxArea, h*(len(heights) - i ))
        return maxArea