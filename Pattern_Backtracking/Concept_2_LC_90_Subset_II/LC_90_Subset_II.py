#Approach
#1)First we sort the list to ensure the duplicates are adjacent to each other
#2)We will backtracking.
#   -Start with an empty list and at every step we choose to either include or exclude the current element
#3) If the current element is the same as the previous element and the previous element was excluded, then we skip the current element to avoid duplicate subsets

#TC:O(2^N)
#SC:O()


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

            #All subsets that include nums[i]                                   --- This whole operations could be condensed to like below
            curSubset.append(nums[i]) #add the element to subset                   |
            backtrack(curSubset,i+1)  #                                            |    backtrack(curSubset+[nums[i],i+1])
            curSubset.pop()  # pop the element that we just add                    |
            #All subsets that dont include nums[i]                              ----
            while i+1 < n and nums[i]==nums[i+1]:
                i+=1
            backtrack(curSubset,i+1)

        backtrack([],0)
        return ans


#My Approach 2) 
#DFS 
#TC : O(N*2^N)
#SC : O(N*2^N)
class Solution:
  def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
     ans = []
     nums.sort()
    def dfs(s: int, path: List[int]) -> None:
      ans.append(path)
      
      if s == len(nums):
        return

      for i in range(s, len(nums)):
        if i > s and nums[i] == nums[i - 1]:
          continue
        dfs(i + 1, path + [nums[i]])

    dfs(0, [])
    return ans



#Competative Programming Approach 
#1) Get all subsets via recursive backtracking
#2) Then pull out the unique sets from the all subsets
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        all_sets = []
        n = len(nums)
        def backtrack(cur,i):
            if i == n:
                all_sets.append(cur[::])
                return
            
            backtrack(cur+[nums[i]],i+1)
            
            backtrack(cur,i+1)
                   
        backtrack([],0)
        
        #all_sets has all subsets 
        #From all_sets just pick the unique list elements by converting the all_sets list to set
        
        unique_sets = [list(s) for s in set([tuple(l) for l in all_sets])]
        
        return unique_sets 