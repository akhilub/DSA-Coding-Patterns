#Problem Function is increasing
#We are looking for minimum


# Time: O(logn) → O(n)
# Space: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l , r = 0 , n-1
        while l<r:
            mid = (l+r)//2
            
            if nums[mid]==nums[r]:
                r-=1
            elif nums[mid]>nums[r]: #notice here elif is essantial
                l = mid+1
            else:
                r = mid
                
        return nums[l]


#To find maximum value in a rotated sorted array 
'''
return nums[l-1]
'''