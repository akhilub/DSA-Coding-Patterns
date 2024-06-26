#Approach:Binary Search
#TC:O(log(n))
#SC:O(1)

#Read the problem statement, Draw the graph
#binary search boundaries are updated according to it
class Solution:
    def findMin(self, nums: List[int]) -> int:
         l ,r = 0 , len(nums)-1
         while l<r:                # Continue until the search range is exhausted
            mid = floor((l+r)/2)   # Finding the middle index

            # If mid element is greater than the rightmost element, the minimum is on the right side
            if nums[mid]>nums[r]: #Note we are not searching for target (i.e nums[r]) this time we are searching for the smallest value in the rotated sorted array that why we are going to update the left pointer to mid +1
                l = mid+1 
            else:
                r = mid    # Otherwise, the minimum is on the left side or at mid
        return nums[l]   