'''
Recursion
We design a function dfs(root1,root2) to determine whether two binary trees are symmetric. The answer is dfs(root,root).

The logic of the function dfs(root1,root2) is as follows:

If both root1 and root2 are null, then the two binary trees are symmetric, return true.
If only one of root1 and root2 is null, or if root1.val ≠ root2.val, then the two binary trees are not symmetric, return false.
Otherwise, determine whether the left subtree of root1 is symmetric to the right subtree of root2, 
and whether the right subtree of root1 is symmetric to the left subtree of root2. Here we use recursion.

The time complexity is O(n), and the space complexity is O(n). Here, 
n is the number of nodes in the binary tree.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(p,q):
            if not p and not q:
                return True
            if not p or not q or p.val!=q.val:
                return False
            return dfs(p.left,q.right) and dfs(p.right,q.left)
        return dfs(root.left,root.right)
    
    
    
#Another Way of writing above Recursive code

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p is None or q is None:
                return p == q
            return p.val==q.val and dfs(p.left,q.right) and dfs(p.right,q.left)
        
        return dfs(root.left,root.right)
    