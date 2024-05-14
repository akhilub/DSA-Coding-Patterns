#Approach: Modified Binary Search

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binary_search_leftmost(A,T):
            L = 0
            R = len(A)
            while L < R:
                m = floor((L + R) / 2)
                if A[m] < T:
                    L = m + 1
                else:
                    R = m
            return L
        
        def binary_search_rightmost(A,T):
            L = 0
            R = len(A)
            while L < R:
                m = floor((L + R) / 2)
                if A[m] > T:
                    R = m
                else:
                    L = m + 1
            return R - 1
        
        l = binary_search_leftmost(nums,target)
        r = binary_search_rightmost(nums,target)
        
        return [l,r] if target in nums else [-1,-1]





#Competative Programming Approach
# TC:O(N) -->Linear Search
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        n = len(nums)
        for i in range(len(nums)):
            if target == nums[i] and ans[0] == -1:
                ans[0] = i #start value
            if target == nums[n-1-i] and ans[1] == -1:
                ans[1] = n-1-i #end value
        return ans
    



#Approach: Just getting to ans

'''
>>> bisect.bisect_left([1,1,1,2,2,2,7,7,7], 2)
3
>>> bisect.bisect_left([1,1,1,2,2,2,7,7,7], 2+1)
6


>>> bisect.bisect_right([1,1,1,2,2,2,7,7,7], 2)
6
>>> bisect.bisect_right([1,1,1,2,2,2,7,7,7], 2+1)
6


>>> bisect.bisect_left([1,1,1,2,2,2,7,7,7], 0)
0
>>> bisect.bisect_left([1,1,1,2,2,2,7,7,7], 1)
0

# below, even single value for 2, after +1 the index will be different
>>> bisect.bisect_left([1,2,3,4,5], 2)
1
>>> bisect.bisect_left([1,2,3,4,5], 2+1)
2
'''

import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = bisect_left(nums, target)
        r = bisect_left(nums, target + 1)
        return [-1, -1] if l == r else [l, r - 1]