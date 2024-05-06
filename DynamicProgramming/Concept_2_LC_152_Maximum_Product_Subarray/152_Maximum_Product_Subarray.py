class Solution:
    def maxProduct(self,nums):
        ans = nums[0] 
        dpMin = nums[0] #The min so far
        dpMax = nums[0] #The max so far
        for i in range(1,len(nums)):
            num = nums[i]
            prevMin = dpMin  #dp[i-1]
            prevMax = dpMax  #dp[i-1]
            if num < 0:
                dpMin = max(prevMax*num,num)
                dpMax = min(prevMin*num,num)
            else:
                dpMin=min(prevMin*num,num)
                dpMax=max(prevMax*num,num)
            ans = max(ans,dpMax)
        return ans        