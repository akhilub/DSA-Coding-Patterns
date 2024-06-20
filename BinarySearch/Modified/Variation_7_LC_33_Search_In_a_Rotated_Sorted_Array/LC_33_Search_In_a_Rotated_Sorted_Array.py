#Approach :Binary Seaech

# We define the left boundary l = 0 and the right boundary r = n - 1 for the binary
# search, where n is the length of the array.

# During each binary search process, we get the current midpoint mid = (l+ r)/2.
# • If nums[mid] >= nums[l], it means that [l, mid] is ordered. At this time, if nums[l] ≤ target < nums[mid], it means that target is in [l, mid], otherwise target is in [mid + 1, r].

# • If nums[mid] < nums[r], it means that [mid + 1, r] is ordered. At this time, if nums[mid] < target ≤ nums[r], it means that target is in [mid + 1, r], otherwise target is in [l, mid].

# • If nums[mid] = nums[r], it means that the elements nums[mid] and nums[r] are equal. At this time, we cannot determine which interval target is in, so we can only decrease r by 1.
# • If nums[mid] = nums[l], it means that the elements nums[mid] and nums[l] are equal. At this time, we cannot determine which interval target is in, so we can only increase l by 1.

# After the binary search ends, if nums [l] = target, it means that the target value `target`
# exists in the array, otherwise it means it does not exist.

# The time complexity is approximately O(log n), and the space complexity is O(1).
# Here, n is the length of the array.

# The time complexity is O(log n), where n is the length of the array nums. The space complexity is O(1).


#Learn this , this is the Binary Search in a Rotated array containing duplicates 
#and write this in interviews

class Solution:
      def search(self, nums: List[int], target: int) -> int:
        
        n=len(nums)
        l,r=0,n-1
        while l<=r:
            mid=(l+r)//2
            
            if nums[mid] ==target: #pitfall see nums[mid]==target not mid ==target , mid is the index value
                return mid
            
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
            
            elif nums[l]<=nums[mid]:  # left half array nums[l..m] are sorted
                if nums[l]<=target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else: # #right half array nums[m..n - 1] are sorted
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
            
            
        return -1








