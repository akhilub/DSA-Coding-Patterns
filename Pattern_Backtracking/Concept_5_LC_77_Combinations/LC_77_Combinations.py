# Backtracking Templates (Two Ways)

#Iterative (I prefer this because simple to visulize)
from copy import deepcopy

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def dfs(s: int, path: List[int]) -> None:
            # no need to check len(t)>k, when '==k' returned already
            if len(path)==k:
                ans.append(deepcopy(path))     #we need deepcopy of path i.e deepcopy(path) instead of path.copy() or path[:] or path[::] even though they all works fine
                return
            
            #here we are only traversing down the path where we want to pick    
            for i in range(s,n+1):
                dfs(i+1,path+[i])
        
        dfs(1,[]) # 1 to n
        return ans
        
        
#Recursive
from copy import deepcopy        
        
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def dfs(s: int, path: List[int]) -> None:
            if len(path)==k:
                ans.append(deepcopy(path))   
                return 
            
            if s>n:
                return
            
            dfs(s+1,path+[s]) #pick
            dfs(s+1,path)     #not pick or skip
            
            
        dfs(1,[])
        return ans
        
        
        
        
        