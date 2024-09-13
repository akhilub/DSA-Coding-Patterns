#Approach:Simulation:
#TC:O(n)

'''
We can iterate through the array, using a variable cnt to record the current number of consecutive 1s, and another variable 
ans to record the maximum number of consecutive 1s.

When we encounter a 1, we increment cnt by one, and then update ans to be the maximum of cnt and ans itself i.e ans=max(ans,cnt). 

Otherwise, we reset cnt to 0.

After the iteration ends, we return the value of ans.

The time complexity is O(n), where n is the length of the array. The space complexity is O(1).

'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        cnt = 0
        for r in range(len(nums)):             
            if nums[r]==1:                          
                cnt+=1
                ans = max(ans,cnt)
            else:
                cnt =0
        return ans
    

'''
for num in nums:
    if num==1:
    
        ||
        ||equivalent to 
        ||   
        
for r in range(len(nums)):             
    if nums[r]==1:  

'''
#Another way of writing same above approach
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        cnt = 0
        for num in nums:
            if num==1:
                cnt+=1
                ans =max(ans,cnt)
            else:
                cnt = 0
                
        return ans
    
    