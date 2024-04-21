#nums = [1,2,3]
#
#           nums[i]
#            /   \
#          pick  skip
#


class Solution:
    def subsets(self,nums):
        ans = []
        def backtrack(cur,i):
            if i == n:
                ans.append(cur[:])     #ans.append(copy.deepcopy(cur))  # cur[:] means deepcopy of 
                return 
            #pick
            backtrack(cur+[nums[i]],i+1)
            #skip
            backtrack(cur,i+1)

        backtrack([],0)
        return ans