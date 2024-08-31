#Approach:Two pointer +Swapping
#TC : O(n)
#SC : O(1)

'''
We define three pointers `left`, `right` and `curr`. 

Pointer left is used to point to the leftmost boundary of the elements with a value of 2 in the array. and 
Pointer right is used to point to the rightmost boundary of the elements with a value of 0 in the array, and 

Initially, `left` = 0 , `right` = n-1 , 
Pointer `curr` is used to point to the current element being traversed, initially `curr`=0.

When curr<=right, we perform the following operations:

If nums[curr]=0, then swap it with nums[left], then increment both left and curr by 1;

If nums[curr]=2, then swap it with nums[right], then decrement right by 1;

If nums[curr]=1, then increment curr by 1.

After the traversal, the elements in the array are divided into three parts: [0,left], [left+1,right-1] and [right,n-1].

The time complexity is O(n), where n is the length of the array. Only one traversal of the array is needed. 
The space complexity is O(1).
'''



# You can also use l ,r, i to reperesent left,right,curr pointers
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0                    # The next 0 should be placed in `left`
        right =len(nums)-1          # THe next 2 should be placed in `right`.
        curr =0
        while curr<=right:
            if nums[curr]==0:
                nums[left],nums[curr]=nums[curr],nums[left]
                left+=1
                curr+=1
                
            elif nums[curr]==2:
                # We may swap a 0 to index `curr`, but we're still not sure whether this 0
                # is placed in the correct index, so we can't move pointer `curr`.
                nums[curr],nums[right]=nums[right],nums[curr]
                right-=1
            else:
                curr+=1










