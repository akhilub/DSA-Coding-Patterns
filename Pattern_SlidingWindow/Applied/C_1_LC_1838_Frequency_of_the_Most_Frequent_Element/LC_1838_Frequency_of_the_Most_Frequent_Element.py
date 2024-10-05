#Approach : PrefixSum (via Sliding Window (Sorting +Two Pointers))

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        ans = 0
        S = 0                                       #S - prefixSum/to accumulate elements val
        nums.sort()
        l =0
        for r , num in enumerate(nums):
            S+=nums[r]
            if S+k < num * (r-l+1):                #while S+k < num * (r-l+1):
                S-=nums[l]
                l+=1
            ans = max(ans,r-l+1)
                
        return ans
















#Approach: No of Operations (via Sliding Window  (Sorting +Two Pointers))

'''

We can first sort the array nums, then enumerate each number as the most frequent element, 
and use a sliding window to maintain the number of operations to increase all numbers from index l to r to nums[r]. 

If the number of operations is greater than k, the left end of the window moves to the right until the number of operations is less than or equal to k. 

In this way, we can find out the maximum frequency for each number as the most frequent element.
The time complexity is O(n x logn), and the space complexity is O(logn). Where n is the length of the array nums.

'''


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        ans = 1
        S = 0                                       #S - no of operations
        nums.sort()
        l =0
        for r in range(1,len(nums)):
            S+=(nums[r]-nums[r-1])*(r-l)
            while S > k:                            
                S-=(nums[r]-nums[l])
                l+=1
            ans = max(ans,r-l+1)
                
        return ans






