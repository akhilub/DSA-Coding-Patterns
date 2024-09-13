# nums = [1,1,1,0,0,0,1,1,1,1,0]
# k =2

#Sliding window with variable length
#TC:O(n)
#SC:O(1)

#Approach
'''
1)Keep the count of the number of zeros ,max window length, curr window length by (r-l+1)
2)Travserse the array with right pointer ,Increment the zeros count as soon as we see one, keep expanding the window until the window condition becomes invalid
3)When the number of zeros become greater the given count ,start contracting the window size by incrementing the left pointer 
4)Store the max length of window by comparing the curr window length and max window length.
'''


class Solution:
    def longestOnes(self,nums,k):
        max_w = 0      #answer
        num_zeros=0    #current number of zeros
        left =0
        n = len(nums)

        for right in range(n):
            if nums[right]==0:
                num_zeros+=1
            
            while num_zeros>k:
                if num[left]==0:
                    num_zeros-=1
                left+=1

            w = right - left +1
            max_w=max(max_w,w)
        
        return max_w

#Explanation:
'''
We can iterate through the array, using a variable `cnt` to record the current number of 0s in the window. 
When `cnt>k`, we move the left boundary of the window to the right by one position.
After the iteration ends, the length of the window is the maximum number of consecutive 1s.


Note that in the process above, we do not need to loop to move the left boundary of the window to the right. 
Instead, we directly move the left boundary to the right by one position. 
This is because the problem asks for the maximum number of consecutive 1s, so the length of the window will only increase, not decrease. 
Therefore, we do not need to loop to move the left boundary to the right.

The time complexity is O(n), where n is the length of the array. The space complexity is O(1).
'''