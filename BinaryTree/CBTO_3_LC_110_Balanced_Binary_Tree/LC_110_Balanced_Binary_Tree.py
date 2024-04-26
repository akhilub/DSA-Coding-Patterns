#Bottom Up recursive DFS to check binary tree is balanced
#A binary tree is balanced 
# 1) as long as its left and right subtrees are balanced (for every node in recursive defination)
# 2) also the height of left subtree and right subtree is no more than 1


#Approach:We will return a tuple where the first value indicates if the current tree is balanced, and the second value is the height of the tree. 
#The time complexity is O(N).


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return True,0
            
            leftBalanced,leftHeight = dfs(root.left)
            if not leftBalanced:
                return False,0
            
            rightBalanced,rightHeight = dfs(root.right)
            if not rightBalanced:
                return False,0
            
            return abs(leftHeight-rightHeight) <=1, 1+max(leftHeight,rightHeight)
        return dfs(root)[0]
    

