#Approach :Recursion

'''
We can pass a window of lower and upper bounds into the recursive function that will check the nodes in the current sub-tree to see if the nodes fall within the range. 
When we go to the left sub-tree, we update the upperbound of the window, similarly when we visit the right subtree, we update the lowerbound of the ranges.

At any time, if a node falls outside its current window, we immediately invalidate the result as not being a valid Binary Search Tree.

As each node has to be checked exactly once, the time complexity is O(N). The space complexity is O(N) as we are using Recursion (which implicitly has caller stacks).

The BST definition is recursive: A valid BST’s left sub trees are all valid BSTs and so are its right sub trees. Therefore, we can solve this problem using Recursive algorithm.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root,minv:int,maxv:int):
            if root is None:    # if not root:
                return True
            
            if root.val<=minv or root.val>=maxv:
                return False
            
            return dfs(root.left,minv,root.val) and dfs(root.right,root.val,maxv)
        
        return dfs(root,-inf,inf) #dfs(root,minv = -float("inf"),maxv = float("inf"))


'''
if root.val<=minv or root.val>=maxv:
    return False
            
return dfs(root.left,minv,root.val) and dfs(root.right,root.val,maxv)

                ||
                ||equivalent
                ||
                
return minv < root.val < maxv and dfs(root.left, minv, root.val) and dfs(root.right, root.val, maxv)

'''
    
# Above Explanation
# In-order traversal. 
# If it is a valid binary search tree, then the sequence traversed should be monotonically increasing. 
# So, we only need to compare and judge whether the current number traversed is greater than the previous number.

# Alternatively, consider the subtree with `root` as the root, whether all node values are within the valid range, and judge recursively.

# The time complexity is O(n), and the space complexity is O(n). 
# Here, n is the number of nodes in the tree.

'''
Note: remember below in invalid, 7 should go right of 5
   5
  / \
 1   8
  \   \
   7   10
'''


#No need to go for BFS , this approach is good and better