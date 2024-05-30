#No memory DP

class Solution:
    def maxProduct(self,nums):
        ans = nums[0] 
        dpMin = nums[0] #The min so far
        dpMax = nums[0] #The max so far
        for i in range(1,len(nums)): # we are starting from index position 1
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



#Clean Simple way of writing
#TC:O(n)
#SC:O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]

        for num in nums[1:]:
            if num < 0:
                max_product, min_product = min_product, max_product

            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)

            result = max(result, max_product)

        return result