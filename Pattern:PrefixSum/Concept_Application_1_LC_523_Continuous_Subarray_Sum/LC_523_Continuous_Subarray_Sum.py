#Approach:PrefixSum

class Solution:
    def checkSubarraySum(self,nums,k):
        s = 0                                   #Intialize prefixSum
        mp = Counter({0:-1})                    #mapping remainder to end index , initialize with 0 remainder to last index

        for i , v in enumerate(nums):
            s+=v                                
            rem = s % k

            #apply question good subarray conditions
            if rem in mp and i - mp[rem] >=2:
                return True

            if rem not in mp:
                mp[rem] = i
        
        return False

        