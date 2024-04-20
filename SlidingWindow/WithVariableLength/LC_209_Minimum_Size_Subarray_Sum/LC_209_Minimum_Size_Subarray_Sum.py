#Sliding window with variable length

#Input: target = 7,nums = [2,3,1,2,4,3]
#Output:2

#TC:O(N)
#SC:O(1)
import math
class Solution:
    def minSubArray(self,target,nums):
        min_w = math.inf  #intialize the min width to be +ve inf  or float('inf) 
        win_sum = 0 # initialize the sum of current window
        left = 0 # initialize the start of the current window
        n =len(arr):
        for right in range(n):
            win_sum+=arr[right] #Add the next ele to the curr wind sum
            #Contract the window as small as possible until the win sum is smaller than target
            while win_sum>=target:  # Window condition broken
                w = right - left +1 # calculate the curr win width
                min_w = min(min_w,w) #update the min_width
                win_sum-=nums[left] #remove the element going out of the win
                left+=1 # slide the win ahead

        if min_w == math.inf:
            return 0
        return min_w


#Follow Up Using Binary Search in O(nlogn)# Ignore .DS_Store files
.DS_Store
