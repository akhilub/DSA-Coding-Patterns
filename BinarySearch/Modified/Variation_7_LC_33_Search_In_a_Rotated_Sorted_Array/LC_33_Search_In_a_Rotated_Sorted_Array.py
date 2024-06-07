# Approach: Binary Search

# We use binary search to divide the array into two parts, [left,..mid] and [mid + 1,..right].

# At this point, we can find that one part must be sorted.

# Therefore, we can determine whether target is in this part based on the sorted part:

# • If the elements in the range [0,..mid] form a sorted array:
#     -If nums[0] <= target <= nums mid, then our search range can be narrowed down to [left,..mid];
#     - Otherwise, search in [mid + 1,..right];

# • If the elements in the range [mid + 1, n - 1] form a sorted array:
#     - If nums mid < target <= nums|n - 1], then our search range can be narrowed down to [mid + 1, ..right];
#     - Otherwise, search in [left,.. mid]

# The termination condition for binary search is left>=right.

# If at the end we find that nums[left] is not equal to target, it means that there is no element with a value of target in the array, and we return -1. 
# Otherwise, we return the index left.

# The time complexity is O(log n), where n is the length of the array nums. The space complexity is O(1).


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l , r = 0 ,n-1
        while l<=r:

            mid = floor((l+r)/2)

            if nums[mid]==target:
                return mid

            elif nums[0]<=nums[mid]: #left array is sorted
                if nums[0]<=target<=nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
        
            else: #right array is sorted
                if nums[mid]<target<=nums[n-1]:
                    l = mid+1
                else:
                    r = mid-1

        return -1






