#Approach:Binary Search

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
            
            #condition to check for duplicates , you can skip this if condition if you want
            if nums[l] == nums[mid] == nums[r]: #to skip the same elements/or identical values/duplicates 
                l += 1
                r -= 1
            
            elif nums[mid]>=nums[l]:  # left half array nums[l..m] are sorted
                if nums[l]<=target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else: #nums[l]>nums[mid]  #right half array nums[m..n - 1] are sorted
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
            
            
        return -1








