#Approach:Two pointer +Swapping
#TC : O(n)
#SC : O(1)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0 # The next 0 should be placed in left
        right =len(nums)-1 # THe next 2 should be placed in right.
        curr =0
        while curr<=right:
            if nums[curr]==0:
                nums[left],nums[curr]=nums[curr],nums[left]
                left+=1
                curr+=1
            elif nums[curr]==2:
                 # We may swap a 0 to index i, but we're still not sure whether this 0
                # is placed in the correct index, so we can't move pointer i.
                nums[curr],nums[right]=nums[right],nums[curr]
                right-=1
            else:
                curr+=1










