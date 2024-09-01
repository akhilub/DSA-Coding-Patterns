#Approach:Sliding window with variable length
#TC:O(n)
#SC:O(1)
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        
        ans, prod , l =0 ,1 ,0
        
        for r in range(len(nums)):
            prod = prod*nums[r]          #append input[right] to window
            
            while prod>=k:               #while INVALID WINDOW CONDITION
                prod = prod//nums[l]     #remove input[left] from window
                l+=1                     
            
            ans = ans+(r-l+1)            # update ans window is valid here
            
        return ans