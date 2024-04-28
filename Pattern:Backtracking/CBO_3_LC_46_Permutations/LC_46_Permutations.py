#Approach

#Recursive Backtrack
#1) We will keep one list(curSol) to keep the track of the element we visited in the nums
#2) Recursively we pass this list and keep on adding the elements that are different 
#3) Stopping condition is when we have reached the total length of array (nums) meaning there are no more permutation


#Input: nums = [1,2,3]
#Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

class Solution:
    def permute(self,nums):
        ans = []
        n =len(nums)

        def backtrack(curSol, i):
             # i tells the depth of the recursive call
            if i == n:
                ans.append(deepcopy(curSol))
                return 

           for ele in nums:
            if ele not in curSol:
                curSol.append(ele)
                backtrack(curSol,i+1)
                curSol.pop()
        
        backtrack([],0)
        return ans


#Approach 2 
#Standard Backtrack DFS
class Solution:
  def permute(self, nums: List[int]) -> List[List[int]]:
    ans = []
    used = [False] * len(nums)

    def dfs(path: List[int]) -> None:
      if len(path) == len(nums):
        ans.append(path.copy())
        return

      for i, num in enumerate(nums):
        if used[i]:
          continue
        used[i] = True
        path.append(num)
        dfs(path)
        path.pop()
        used[i] = False

    dfs([])
    return ans