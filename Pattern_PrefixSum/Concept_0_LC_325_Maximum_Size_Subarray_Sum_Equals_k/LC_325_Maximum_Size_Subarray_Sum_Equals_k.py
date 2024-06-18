#Approach: PrefixSum
#TC:O(n)
#SC:O(n)
# Setting d[0] = -1 ensures that if at any point the prefix (cumulative sum) becomes k, prefix - k (which is 0 in this case) will correctly retrieve the starting index -1 from the dictionary, indicating a valid subarray of length i - (-1) = i + 1.
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        d = {0:-1} #to store prefixSum with their indices
        s = 0 # to store prefixSum/cumulative Sum as we iterate through the array 
        ans = 0 # to keep track of max length of subarray whose sum is equal to k
        for i , v in enumerate(nums):
            s+=v 
            if s - k in d:                    #Here remSum = s-k
                ans = max(ans,i-d[s-k])
            if s not in d:
                d[s]=i
        return ans
