#Approach : Monotonic Stack (Increasing)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1]*n
        stk = [] #an increasing stack
        
        for i in range(2*n-1,-1,-1):
            i = i%n 
            while stk and stk[-1]<=nums[i]:
                stk.pop()
            if stk:
                ans[i]=stk[-1]
            stk.append(nums[i])
        return ans





#Approach : Monotonic Stack (Decreasing)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1]*n
        stk = [] #a decreasing stack storing indices

        for i in range(2*n):
            num = nums[i%n]
            while stk and nums[stk[-1]]<num:
                ans[stk.pop()]=num
            if i<n:
                stk.append(i)

        return ans
    
    
    



