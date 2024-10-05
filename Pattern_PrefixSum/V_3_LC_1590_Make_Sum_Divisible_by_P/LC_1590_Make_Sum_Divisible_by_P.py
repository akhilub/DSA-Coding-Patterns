#Approach:PrefixSum
#TC:O(n)
#SC:O(min(n,p))

#Algorithm

'''
1. Calculate the total sum of the array nums and find the remainder rem when divided by p.
2. If rem is 0, return 0 since the sum is already divisible by p.
3. Initialize ans to the length of the array (maximum subarray size).
4. Use a variable S to keep track of the running prefix sum, and a hashmap cnt to store the remainder of S % p and the corresponding index.
5. Iterate over the array:
 • Update the prefix sum and calculate S % p.
 • Calculate the target remainder that would help balance the remainder rem.
 • If target exists in the hashmap, update ans with the smaller value between ans and the current subarray length.
 • Store the current prefix sum's remainder and index in cnt.
6. If ans is still equal to the array length, return -1. Otherwise, return ans.
'''

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        summ = sum(nums)
        rem = summ % p

        if rem == 0:
            return 0
        
        ans = len(nums)
        S = 0
        #a hashmap (dictionary) to store prefix sum remainder and their indices where that remainder is seen.
        # Initially, store remainder 0 at index -1 to handle edge cases like prefix subarrays.
        cnt = {0: -1}
        
        for i, num in enumerate(nums):
            S = (S + num) % p
            target = (S - rem) % p              #target(the remainder we need to remove) and check if we've seen it before.
            
            if target in cnt:
                ans = min(ans, i - cnt[target])
            
            cnt[S] = i
        
        return -1 if ans == len(nums) else ans


