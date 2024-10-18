#Approach
'''

To solve this problem, we can use a similar approach to 3Sum, leveraging sorting and the two-pointer technique. 
We will reduce the problem by fixing two numbers and using the two-pointer technique to find the remaining two numbers.

Time complexity:
𝑂(𝑛3), where 𝑛 is the length of the array. Sorting the array takes 𝑂(𝑛 log 𝑛), and the three nested loops (with the two-pointer approach) take 𝑂(𝑛3) in total.


Space complexity:
O(1), ignoring the space needed for the output list. We only use a few extra variables to keep track of indices.

'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []                            
        for i in range(n-3):
            if i>0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i+1,n-2):
                if (j > i + 1 and nums[j] == nums[j - 1]):
                    continue
                
                l,r = j+1,n-1
                while l<r:
                    summ = nums[i]+nums[j]+nums[l]+nums[r]
                    
                    if summ==target:
                        ans.append([nums[i],nums[j],nums[l],nums[r]])
                        
                        while (l < r and nums[l] == nums[l+1]):
                            l+=1
                            
                        while (l < r and nums[l] == nums[r-1]):
                            r-=1
                            
                        l,r=l+1,r-1
                    elif summ<target:
                        l+=1
                    else:
                        r-=1
                    
                    
        return ans













#Approach: Sorting+ Two Pointer (using set) 
#TC:O(n³)
#SC:O(m)


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                l,r = j+1,len(nums)-1
                while l<r:
                    s = nums[i]+nums[j]+nums[l]+nums[r]
                    if s == target:
                        ans.add((nums[i],nums[j],nums[l],nums[r]))
                        r-=1
                        l+=1
                    elif s > target:
                        r-=1
                    else:
                        l+=1
                  
        return ans                  #Note: ans is a set containing tuple of all the unique quadruplets
        #return [list(tup) for tup in ans]

