#Approach:Sliding Window flexible Longest
#TC:O(N)
#SC:O(N)
from collections import Counter
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        l = 0
        cnt = Counter()
        for r in range(n):
            cnt[nums[r]]+=1     #add the count of incoming element
            while cnt[nums[r]]>k: #Think/Check for condition when the window condition become invalid (flip this An array is called good if the frequency of each element in this array is less than or equal to k)
                cnt[nums[l]]-=1 #decrease the count of incoming element
                l+=1            #slide the window 
            ans = max(ans,r-l+1) #update the answer
            
        return ans