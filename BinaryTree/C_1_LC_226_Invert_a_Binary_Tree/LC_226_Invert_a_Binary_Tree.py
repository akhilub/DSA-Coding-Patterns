# Approach : Using Recursion to invert a Binary tree
# The terminal case is to invert a None node which is None
# Now just recursively invert left and right subtrees and assign it to right and left pointers

# TC:O(N) 
# SC:O(N)
# where N is the no of nodes in the binary Tree

#Defination of binary Tree
#class TreeNode:
#   def __init__(self,val =0,left=None,right=None):
#       self.val = val
#       self.left = left
#       self.right =right

class Solution:
    def invertTree(self,root):
        if root is None:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root


