#Fundamental approach :PrefixSum

#TC:O(N)
#SC:O(N)
class Solution:
    def subarraySum(self,nums,k):
        prefixSum = 0
        hashMap = {0:1} # will store the frequencies of prefixSum
        ans = 0 #count of subarray sum equals to k
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
# Write using this in interviews
class Solution:
    def subarraySum(self,nums,k):
        prefixSum = 0
        hashMap = {0:1} # will store the frequencies of prefixSum
        ans = 0
        for i in range(len(nums)):
            prefixSum+=nums[i]
            remSum  = prefixSum - k 
            
            if remSum in hashMap:
                ans+=hashMap[remSum]
            
           hashMap[prefixSum] = hashMap.get(prefixSum, 0) + 1

        return ans


#Competative Programming Approach
#Loop over nums and calculate the total sum `s`.For each num in nums,add num to sum `s`
#and obtain the count of subarrays with sum `s- k`.Add the sum `s` to the result `ans`.
#Then update the map `cnt` with the count of subarrays with sum `s`.Finally return the result `ans`.


'''
We define a hash table `cnt` to store the number of times the prefix sum of the array `nums` appears. 
Initially, we set the value of `cnt[0]` to `1`, indicating that the prefix sum `0` appears once.

We traverse the array `nums`, calculate the prefix sum `s`, then add the value of `cnt[s - k]` to the answer, and increase the value of `cnt[s]` by 1.

After the traversal, we return the answer.

The time complexity is O(n), and the space complexity is O(n). Where n is the length of the array nums.

'''

class Solution:
    def subarraySum(self,nums,k):
        cnt = Counter({0:1})
        ans = s = 0
        for num in nums:
            s+=num                                                            
            ans+=cnt[s-k]                               
            cnt[s]+=1                                  
        return ans



'''
s+=num                                                            
ans+=cnt[s-k]                               
cnt[s]+=1 

    ||
 equivalent
    ||
    
s+=num
remS =s-k
ans+=cnt[remS]
cnt[s]+=1
'''