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