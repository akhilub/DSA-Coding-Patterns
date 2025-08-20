#Approach : DFS Recursion
#TC:O(n)
#SC:O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans=[]
        def dfs(root,path):
            #terminate dfs
            if not root:
                return 
            
            path.append(str(root.val)) #list containing node values in string type
            
            #leaf node
            if not root.left and not root.right:
                ans.append('->'.join(path[:])) #string manipulation
            
            dfs(root.left,path)
            dfs(root.right,path)
            path.pop()
            
    
        dfs(root,[])
        return ans