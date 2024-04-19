# nums = [1,1,1,0,0,0,1,1,1,1,0]
# k =2

#Sliding window with variable length
#TC:O(n)
#SC:O(1)

#Approach
#1)Keep the count of the number of zeros ,max window length, curr window length by (r-l+1)
#2)
#3)Travserse the array with right pointer ,Increment the zeros count as soon as we see one, keep expanding the window until the window condition becomes invalid
#4)When the number of zeros become greater the given count ,start contracting the window size by incrementing the left pointer 
#5)Store the max length of window by comparing the curr window length and max window length.
class Solution:
    def longestOnes(self,nums,k):
        max_w = 0
        num_zeros=0
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

            