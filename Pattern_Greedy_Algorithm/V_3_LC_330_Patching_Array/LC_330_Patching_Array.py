#Approach:Greedy Algorithm
#TC:O(m+log(n))   , where m is the length of the array nums
#SC:O(1)

from typing import List
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ans = 0
        i = 0                                                               #nums' index
        miss = 1                                                            #the minimum sum in [1, n] we might miss#
        while miss<=n:
            if i<len(nums) and nums[i]<=miss:
                miss+=nums[i]
                i+=1
            else:
                '''Greedily add `miss` itself to increase the range from [1, miss) to [1, 2 * miss)'''
                miss = 2*miss #or  miss<<=1  or  # miss+=miss               #Double the current `miss`  
                ans+=1
        return ans
    
    
print(Solution().minPatches([1,3],6))
print(Solution().minPatches([1,5,10],20))
print(Solution().minPatches([1,2,2],5))
