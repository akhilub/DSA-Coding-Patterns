# Approach:Simulation

'''
We can simulate the problem directly according to the requirements.

The time complexity is O(n), where n is the length of the array nums. Ignoring the space consumption of the answer, the space complexity is O(1).
'''

from typing import List
from itertools import pairwise
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        n = len(nums)
        if n==0:return [[lower,upper]]
        
        ans = []
        if nums[0]>lower:
            ans.append([lower,nums[0]-1])
        
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]>1:
                ans.append([nums[i-1]+1,nums[i]-1])
        
        if nums[-1]<upper:
            ans.append([nums[-1]+1,upper])

        return ans


'''
for i in range(1,len(nums)):
    if nums[i]-nums[i-1]>1:
        ans.append([nums[i-1]+1,nums[i]-1])

            ||
            ||equivalent
            ||
            
for prv,cur in pairwise(nums):
    if cur-prv>1:
        ans.append([prv+1,cur-1])

'''




if __name__=="__main__":
    nums = [0,1,3,50,75] 
    lower = 0 
    upper = 99
    print("TestCase1",Solution().findMissingRanges(nums,lower,upper))
    
    
    


'''
>>> pairwise([0,1,3,50,75])
<itertools.pairwise object at 0x10472a080>
>>> list(pairwise([0,1,3,50,75]))
[(0, 1), (1, 3), (3, 50), (50, 75)]
'''
    
    
    
    
