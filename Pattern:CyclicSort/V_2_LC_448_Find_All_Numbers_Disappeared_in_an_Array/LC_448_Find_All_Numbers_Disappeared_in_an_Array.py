from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i , n = 0 ,len(nums)
        missingNumber = []
        while i < n:
            pos = nums[i]-1
            print('pos',pos)
            if nums[i]!=nums[pos]:
                nums[i],nums[pos] = nums[pos],nums[i]
            else:
                i =i+1
        
        for i in range(n):
            if nums[i]!=i+1:
                missingNumber+=[i+1]

        return missingNumber
        



if __name__=="__main__":
    sol = Solution()
    nums = [4,3,2,7,8,2,3,1]
    actual_output = sol.findDisappearedNumbers(nums)
    expected_output = [5, 6]
    print('Test Case 1',actual_output == expected_output)

