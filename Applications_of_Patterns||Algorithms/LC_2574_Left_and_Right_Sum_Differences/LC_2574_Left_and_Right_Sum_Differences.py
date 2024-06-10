#Approach:PrefixSum
#TC:O(n)
#SC:O(n)
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n =len(nums)
        leftSum = [0]*n 
        rightSum = [0]*n 
        differenceSum = [0]*n

        for i in range(1,n):
            leftSum[i] = leftSum[i-1]+nums[i-1]

        for i in range(n-2,-1,-1):
            rightSum[i] = rightSum[i+1]+nums[i+1]

        for i in range(n):
            differenceSum[i] = abs(leftSum[i]+rightSum[i])

        return differenceSum

#Optimized PrefixSum
#TC:O(n)
#SC:O(1)
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n =len(nums)
        
        ans = [0]*n
        
        left=0
        for i in range(n):
            ans[i] = left
            left = left+nums[i]
            
        right = 0
        for i in range(n-1,-1,-1):
            ans[i]=abs(ans[i]-right)
            right = right+nums[i]
            
        return ans