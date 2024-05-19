# We maintain a sliding window of length , use a hash table to record the count of each number in the window, and use a variable 
# to record the sum of all numbers in the window. Each time we slide the window, if all numbers in the window are unique, we update the answer.

#TC:O(n)
#SC:O(n)

class Solution:
    def maximumSubarraySum(self,nums,k):
        cnt = Counter(nums[:k])
        s = sum(nums[:k])
        ans = s if len(cnt)==k else 0
        for i in range(k,len(nums)):
            #add the incoming ele from right
            cnt[nums[i]]+=1
            s+=nums[i]
            #subtract the outgoing ele from left it is at position (right - k)
            cnt[nums[i-k]]-=1
            s-=nums[i-k]
            #apply conditions
            #1)#apply condition all elements needs to be distinct in window/subarray?
            #How? by checking the key value in the hashtable when 0 remove that key
            if cnt[nums[i-k]]==0:
                del cnt[nums[i-k]]
            #2)#apply condition length of subarray needs to be k and distinct
            if len(cnt)==k:
                ans = max(ans,s)
            return ans


