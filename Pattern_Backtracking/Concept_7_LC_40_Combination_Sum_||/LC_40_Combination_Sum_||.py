#Approach:DFS
#1) Sort the candidate list so that we can skip the loop when the adjacent element are identical in the candidates list while picking them in the path 

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        
        def dfs(path:List[int],s:int):
            if sum(path)==target:
                ans.append(path[::])
                return
            
            if sum(path) > target:
                return
            
            for i in range(s,n):
                if i > s and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                dfs(path,i+1)   #Here we are passing i+1 because we can only select the element from candidate list only once to path list
                path.pop()
                
        candidates.sort()
        dfs([],0)
        return ans
      

'''
```
path.append(candidates[i])
dfs(path,i+1)
path.pop()
```


equivalent

```
dfs(path+[candidates[i]],i+1)
```



'''      




#Another way of Writing same above approach,if you cannot use the inbuilt sum method
class Solution:
  def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    ans = []

    def dfs(s: int, target: int, path: List[int]) -> None:
      if target < 0:
        return
      if target == 0:
        ans.append(path.copy())
        return

      for i in range(s, len(candidates)):
        if i > s and candidates[i] == candidates[i - 1]:
          continue
        path.append(candidates[i])
        dfs(i + 1, target - candidates[i], path)
        path.pop()

    candidates.sort()
    dfs(0, target, [])
    return ans