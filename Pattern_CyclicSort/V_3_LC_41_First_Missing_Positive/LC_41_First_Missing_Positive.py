#Approach : Using Modified Cyclic Sort

#We assume the length of the array nums is n, then the smallest positive integer must be in the range [1,.., n + 1]. 
#We can traverse the array and swap each number x to its correct position, that is, the position x - 1. 
#If x is not in the range [1, n + 1], then we can ignore it.
#After the traversal, we traverse the array again. If i + 1 is not equal to nums(i], then i + 1 is the smallest positive integer we are looking for.

#TC:O(n)
#SC:O(1)

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i , n = 0 , len(nums)
        while i < n:
            pos = nums[i]-1
            if 1<=nums[i]<=n and nums[i]!=nums[pos]: #add the modified question condition "smallest positive integer that is not present in nums" which translates to nums[i] is between 1 and n
                nums[pos],nums[i] = nums[i],nums[pos]
            else:
                i = i+1

        for i in range(n):
            if nums[i]!=i+1:
                return i+1

        return n+1  # added to satisfy the question condition


# Correct slot:
# nums[i] = i + 1
# nums[i] - 1 = i
# nums[nums[i] - 1] = nums[i]