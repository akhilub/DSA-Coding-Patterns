#Approach: DFS+PrefixSum

#We can consider each path as a subarray and calculate its prefix sum to find any required sub paths

class Solution:
    def pathSum(self,root,targetSum):
        def dfs(node,pathSum):
            if node is None:
                return 0
            
            pathSum+=node.val     

            ans = prefixSum[pathSum-targetSum]      # The number of paths that have the required sum.

            prefixSum[pathSum]+=1

            ans+=dfs(node.left,pathSum)
            ans+=dfs(node.right,pathSum)

            pathSum-=1

            return ans

        prefixSum = Counter({0:1})
        return dfs(root,0)


#Just another way of writing

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, s):
            if node is None:
                return 0
            s += node.val
            ans = cnt[s - targetSum]
            cnt[s] += 1
            ans += dfs(node.left, s)
            ans += dfs(node.right, s)
            cnt[s] -= 1
            return ans

        cnt = Counter({0: 1})
        return dfs(root, 0)