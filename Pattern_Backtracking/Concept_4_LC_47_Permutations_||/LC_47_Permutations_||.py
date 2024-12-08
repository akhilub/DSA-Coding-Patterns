#Approach 1
#1) Find All Permutations
#2) Create a hashMap to check if we have already seen that permutation before to prune that branch









#Approach 2
#Standard DFS
class Solution:
    def permuteUnique(self,nums):
        ans = []
        used = [False]*len(nums)
        nums.sort()

        def dfs(path):
            if len(path)==len(nums):
                ans.append(path[:])
                return
            
            for i , num in enumerate(nums):
                if used[i]: # skipping the loop / branch of the recursive tree
                    continue
                
                if i>0 and nums[i]==nums[i-1] and not used[i-1]: #skipping the duplicates from the nums
                    continue
                
                used[i] = True
                path.append(num)
                dfs(path)
                path.pop()
                used[i] = False

        dfs([])
        return ans

