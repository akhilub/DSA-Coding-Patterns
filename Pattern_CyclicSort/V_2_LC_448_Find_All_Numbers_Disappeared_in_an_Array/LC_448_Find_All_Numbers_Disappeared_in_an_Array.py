#Approach:Cyclic Sort
#TC:O(n)
#SC:O(1)
from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i , n = 0 ,len(nums)
        while i < n:
            pos = nums[i]-1
            if nums[i]!=nums[pos]:
                nums[i],nums[pos] = nums[pos],nums[i]
            else:
                i =i+1
        
        return [i+1 for i in range(n) if nums[i]!=i+1]
    

'''

missingNumber = []
for i in range(n):
    if nums[i]!=i+1:
        missingNumber+=[i+1]

return missingNumber
    
        ||
    equivalent
        ||
                
return [i+1 for i in range(n) if nums[i]!=i+1]




'''











#When input modification is not allowed
#Approach:Counting
#TC:O(n)
#SC:O(n)

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        count = [1]+[0]*n             # padding for 1-indexed
        for num in nums:
            count[num]+=1
        
        return [i for i,v in enumerate(count) if v==0]
        
        
            

'''
return [i for i,v in enumerate(count) if v==0]

            ||
        better than
            ||
            
ans = []
for i in range(len(count)):
    if count[i]==0:
        ans.append(i)
                
return ans
'''




if __name__=="__main__":
    sol = Solution()
    nums = [4,3,2,7,8,2,3,1]
    actual_output = sol.findDisappearedNumbers(nums)
    expected_output = [5, 6]
    print('Test Case 1',actual_output == expected_output)

