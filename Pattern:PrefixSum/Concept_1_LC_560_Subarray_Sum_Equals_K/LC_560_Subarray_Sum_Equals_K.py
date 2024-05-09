#Fundamental approach
class Solution:
    def subarraySum(self,nums,k):
        prefixSum = 0
        hashMap = {0:1}
        ans = 0
        for i in range(len(nums)):
            prefixSum+=nums[i]
            remSum = prefixSum - k

            if remSum in hashMap:
                ans+=hashMap[remSum]
            
            #Could be condensed see it below
            if prefixSum in hashMap:
                hashMap[prefixSum]+=1
            else:
                hashMap[prefixSum]=1

        return ans


#My Approach
class Solution:
    def subarraySum(self,nums,k):
        prefixSum = 0
        hashMap = {0:1} # will store the frequencies of prefixSum

        for i in range(len(nums)):
            prefixSum+=nums[i]
            remSum  = prefixSum - k 
            
            if remSum in hashMap:
                ans+=hashMap[remSum]
            
           hashMap[prefixSum] = hashMap.get(prefixSum, 0) + 1

        return ans


#Competative Programming Approach
#Loop over nums and calculate the total sum `sum`.For each num in nums,add num to
#sum and obtain the count of subarrays with sum `sum - k`.Add the sum to the result.
#Then update the map with the count of subarrays with sum `sum`.Finally return the result.
class Solution:
    def subarraySum(self,nums,k):
        dp = Counter({0:1})
        ans = s = 0
        for num in nums:
            s+=num
            ans+=dp[s-k]
            dp[s]+=1
        return ans

