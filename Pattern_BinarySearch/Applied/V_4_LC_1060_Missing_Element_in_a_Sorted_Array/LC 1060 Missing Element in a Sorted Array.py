#Approach:Binary Search:
#TC:O(log(n))
#SC:O(1)

from typing import List
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        l , r = 0 , len(nums)-1

        while l<=r:
            mid = (l+r)//2
            # Perform binary search to find the smallest index such that the number of missing elements until that index is at least k
            if nums[mid]-nums[0]-mid <k:
                l = mid+1
            else:
                r = mid-1

        return nums[0]+k+r  #nums[0]+k+(l-1)



# Another Way of writing the above code
from typing import List
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        l, r = 0, len(nums) - 1

        # Calculate the number of missing elements up to the last element
        missing = lambda idx: nums[idx] - nums[0] - idx

        # Perform binary search to find the smallest index such that
        # the number of missing elements until that index is at least k
        while l <= r:
            mid = (l + r) // 2
            if missing(mid) < k:
                l = mid + 1
            else:
                r = mid - 1

        # The kth missing number is nums[0] + k + r
        return nums[0] + k + r





if __name__=="__main__":
    nums = [4,7,9,10]
    k =1
    expected_output = 5
    
    actual_output = Solution().missingElement(nums,k)
    print("TestCase1",actual_output)
    
    
    nums = [4,7,9,10]
    k = 3
    expected_output = 8
    
    actual_output = Solution().missingElement(nums,k)
    print("TestCase1",actual_output)
    
    nums = [1,2,4]
    k = 3
    expected_output = 6
    
    actual_output = Solution().missingElement(nums,k)
    print("TestCase1",actual_output)
    
     