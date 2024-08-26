#Approach:Recursive

#Logic

#Stick to this logic

# If the binary tree is also a Binary Search Tree, then we can utilise the fact that the left nodes are strictly smaller and the right nodes are strict larger. 
# When root is greater than p and q , then the lowest common ancestor is somewhere on the left tree, and when root is smaller than p and q , then the lowest common ancestor is somewhere on the right tree. 
# Otherwise, the root is the lowest common ancestor (since p and q are separate in left/right tree respectively).

# We can do this Recursion (beaware of Stack Overflow risk):


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        
        if root.val>p.val and root.val>q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        
        if root.val<p.val and root.val<q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        
        return root
            
'''
We can do this iteratively by moving the current pointer to left or right. 
The time complexity is O(H) where H is the height of the binary search tree and in worst case H is N – the number of nodes.
'''

#Approach:Iterative

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if root.val>p.val and root.val>q.val:
                root = root.left
            elif root.val<p.val and root.val<q.val:
                root = root.right
            else:
                break
        return root