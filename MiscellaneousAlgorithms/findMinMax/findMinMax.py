#Approach:Simulation
#TC:O(n)
#SC:O(1)

class Solution:
    #Pythonic Way
    def getMinMax(self,nums):
        minN = nums[0]
        maxN = nums[0]
        
        for num in nums[1:]:                    
            if num<=minN:
                minN = num
            
            if num>=maxN:
                maxN = num 
                
        return [maxN,minN]
    
    
    #Using for loop traditionsl index iterative way
    def getMinMax2(self,nums):
        minN = nums[0]
        maxN = nums[0]
        
        for i in range(1,len(nums)):                    
            if nums[i]<=minN:
                minN = nums[i]
            
            if nums[i]>=maxN:
                maxN = nums[i] 
                
        return [maxN,minN]
    
    #DP
    def getMinMax3(self,nums):
        minN = nums[0]                  #float('inf')     
        maxN = nums[0]                  #float('-inf')
        
        for num in nums[1:]:            #for num in nums:
            minN = min(num,minN)                    
            maxN = max(num,maxN)
                
        return [maxN,minN]

    

if __name__=="__main__":
    nums1 = [4, 2, 5, 1, 6, 3]
    actualOutput = [6,1]
    print(Solution().getMinMax(nums1)) 
    print(Solution().getMinMax2(nums1)) 
    print(Solution().getMinMax3(nums1)) 
    
    
    nums2 = [1, 5, 7, 2, 9, 3]
    actualOutput = [9,1]
    print(Solution().getMinMax(nums2)) 
    print(Solution().getMinMax2(nums2)) 
    print(Solution().getMinMax3(nums2)) 
    
    
    nums3 = [4, -2, 5, 1, 6, 3 ,10**9]
    actualOutput = [10**9,-2]
    print(Solution().getMinMax(nums3)) 
    print(Solution().getMinMax2(nums3)) 
    print(Solution().getMinMax3(nums3)) 