class Solution:
      def search(self, nums: List[int], target: int) -> int:
        
        n=len(nums)
        l,r=0,n-1
        while l<=r:
            mid=(l+r)//2
            
            if nums[mid] ==target:
                return True
            
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
            
            elif nums[l]<=nums[mid]:  # nums[l..m] are sorted
                if nums[l]<=target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else: # nums[m..n - 1] are sorted
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
            
            
        return False