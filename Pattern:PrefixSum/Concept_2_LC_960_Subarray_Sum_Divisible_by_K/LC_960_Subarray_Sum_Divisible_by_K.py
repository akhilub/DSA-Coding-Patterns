#My Approach
#TC:O(N) where N is the no of elements in the array
#SC:O(M)
class Solution:
    def subarraysDivByK(self,nums,k):
        prefixSum = 0
        hashMap = {0:1} # will stores the frequencies of remainder
        ans = 0
        for i in range(len(nums)):
            prefixSum+=nums[i]
            rem = prefixSum % k 

            if rem in hashMap:
                ans+=hasMap[rem]
                hashMap[rem]+=1
            else:
                hashMap[rem]=1


#Competative Programming Approach
class Solution:
    def subarraysDivByK(self,nums,k)
    cnt = Counter({0;1})
    ans = s = 0
    for x in nums:
        s = (s+x) % k
        ans+=cnt[k]
        cnt[k]+=1
    return ans