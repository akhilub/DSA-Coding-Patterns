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


