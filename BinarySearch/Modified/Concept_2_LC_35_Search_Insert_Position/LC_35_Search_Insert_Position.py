#Approach:Binary Search
#TC:log(n)

class Soluion:
    def searchInsert(self,nums,target):
        l = 0
        r = len(nums) -1
        while l <= r:
            m = (l+r) // 2

            if nums[m]>target:
                r = m-1
            elif nums[m] <target:
                l = m+1
            else:
                return m
    return l 



#Approach:Competative Programming
import bisect
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = bisect.bisect_left(nums,target)
        return l