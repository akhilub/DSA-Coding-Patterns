class Solution:
    def search(self,nums):
        l = 0 
        r = len(nums) - 1
        while l <=r: #left < = right
            m = (l+r)//2
            if nums[m]>target:
                #update right pointer since target lies in left half
                r = m - 1   
            elif nums[m] < target:
                #update left pointer since target lies in right half
                l = m +1 
            else: # num[m] == target ;found the target
                return m
    
        return -1


#Competative Programming
import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = bisect_left(nums,target)

        return -1 if l==len(nums) or nums[l] !=target else l