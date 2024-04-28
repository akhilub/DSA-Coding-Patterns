#Approach 
#Recursive Backtracking

#1) For every position in candidate we will either pick the element or skip the element in cur list
#2) While picking the element recursively we can pick the same element multiple time 
#3) Terminate the function on various conditions


class Solution:
    def combinationSum(self,candidates):
        ans = []
        n = len(candidates)

        def backtrack(cur,i):
            if sum(cur)==target:
                ans.append(copy.deepcopy(cur))
                return   #Dont Forget to return 

            if i == n or sum(cur) > target:
                return 
    
        #pick the element at position i , given we can pick the same element multiple times to reach to target
        backtrack(cur+[candidate[i]],i) # Here when we are picking we can pick the same element multiple times to reach to target sum i.e why in function backtrack argument i is i and not i+1

        #skip the element at position i and move ahead
        backtrack(cur,i+1)
        backtrack([],0)
        return ans


#My Approach 
#1) Make the recursive decision tree, then we will realize it is a backtracking 
#2) Start the dfs with empty path list and the current level i.e 0
#3) The tree branches are seen through for loop , the for loop starts from the current level
#3)We can pick the same element multiple time from the candidate list in the path list when we are backtracking
#4)Prune the tree meaning return if the sum(path) becomes more than the target
#5)Store/Save the path if sum(path) reaches target
#6)Upon returning from a level pop out the last added elemet in the past list

#TC : O(∣candidates∣^target)
#SC : O(target)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        
        def dfs(path,s):
            if sum(path)==target:
                ans.append(path[::])
                return
            
            if sum(path) > target:
                return
            
            for i in range(s,n):
                path.append(candidates[i])
                dfs(path,i)
                path.pop()
                
            
        dfs([],0)
        return ans


#Approach 
#Standard DFS

# Time: 𝑂(∣candidates∣target)

# Space: 𝑂(target)
class Solution:
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    ans = []

    def dfs(s: int, target: int, path: List[int]) -> None:
      if target < 0:
        return
      if target == 0:
        ans.append(path.clone())
        return

      for i in range(s, len(candidates)):
        path.append(candidates[i])
        dfs(i, target - candidates[i], path)
        path.pop()

    candidates.sort()
    dfs(0, target, [])
    return ans