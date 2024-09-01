#Approach1:Mathematics
#TC:O(n)
#SC:O(n)
'''
We denote `s1` as the sum of all numbers from `[1,..n]`, `s2` as the sum of the numbers in the array 

`nums` after removing duplicates, and `s` as the sum of the numbers in the array `nums`.

Then `s-s2` is the duplicate number, and `s1-s2` is the missing number is the missing number.

The time complexity is O(n), and the space complexity is O(n), where n is the length of the array 
nums. Extra space is needed to store the array after de-duplication.
'''

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s1 = (1 + n) * n // 2
        s2 = sum(set(nums))
        s = sum(nums)
        return [s - s2, s1 - s2]
    
#Approach2:Hash Table
'''
We can also use a more intuitive method, using a hash table `cnt` to count the occurrence of each number in the array `nums`.

Next, iterate through x∈[1,n], 
if cnt[x]=2, then x is the duplicate number, 
if cnt[x]=0, then x is the missing number.

The time complexity is O(n), and the space complexity is O(n), where n is the length of the array nums.
'''

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        n = len(nums)
        ans = [0] * 2
        for x in range(1, n + 1):
            if cnt[x] == 2:
                ans[0] = x
            if cnt[x] == 0:
                ans[1] = x
        return ans



#My Approach:Cyclic Sort 
#TC:O(n)
#SC:O(n)
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        #Cyclic Sort
        n = len(nums)
        i =0
        while i<n:
            pos = nums[i]-1
            if nums[i]!=nums[pos]:
                nums[i],nums[pos]=nums[pos],nums[i]
            else:
                i+=1
                
        c_nums = nums[:]
         
        #Problem Algorithm       
        ans = []
        for i in range(len(c_nums)):
            if i==nums[i]-1:
                continue
            else:
                ans.append(nums[i])
                ans.append(i+1)
        return ans
    
    
#Approach :Bit Operations
#TC:O(n)
#SC:O(1)
#Not required for interviews