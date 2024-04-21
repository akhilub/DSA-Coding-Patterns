#Approach
#1)First we sort the list to ensure the duplicates are adjacent to each other
#2)We will backtracking.
#   -Start with an empty list and at every step we choose to either include or exclude the current element
#3) If the current element is the same as the previous element and the previous element was excluded, then we skip the current element to avoid duplicate subsets

#TC:O(2^N)
#SC:O


class Solution:
    def subsetWithDup(self,nums):
        ans = []
        nums.sort()
        n=len(nums)

        def backtrack(curSubset,i):
            #terminal or base case
            if i == n:
                res.append(curSubset[::])
                return

            #recursive case


            #All subsets that include nums[i]
            curSubset.append(nums[i]) #add the element to subset
            backtrack(curSubset,i+1)
            curSubset.pop()  # pop the element that we just add

            #All subsets that dont include nums[i]
            while i+1 < n and nums[i]==nums[i+1]:
                i+=1
            backtrack(curSubset,i+1)

        backtrack([],0)
        return ans