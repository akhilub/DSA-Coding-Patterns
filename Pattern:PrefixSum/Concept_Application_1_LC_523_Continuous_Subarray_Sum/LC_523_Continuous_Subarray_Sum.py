class Solution:
    def checkSubarraySum(self,nums,k):
        prefixSum = 0
        hashMap = Counter({0:-1}) #mapping remainder to end index , initialize with 0 remainder to last index

        for i , v in enumerate(nums):
            prefixSum+=v 
            rem = prefixSum % k

            #apply question good subarray conditions
            if rem in hashMap and i - hashMap[rem] >=2:
                return True

            if rem not in hashMap:
                hashMap[rem] = i
        
        return False

        