#Approach : DFS Recursion


#We start from the root node, recursively traverse all paths from the root node to the leaf nodes, and record the path sum. 
#When we traverse to a leaf node, if the current path sum equals targetSum, then we add this path to the answer.

#The time complexity is O(n^2), where n is the number of nodes in the binary tree. The space complexity is O(n).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(root,path):
            #termninate dfs
            if root is None:
                return
            
            path.append(root.val)
            
            #leaf node
            if not root.left and not root.right:
                if sum(path)==targetSum: #check for path sum i.e apply question condition
                    ans.append(path[::]) # or path.copy() or path[:]
                    
            dfs(root.left,path)
            dfs(root.right,path)
            path.pop()

        dfs(root,[])  
        return ans