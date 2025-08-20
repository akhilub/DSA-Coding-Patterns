#Solutions
#1. Recusive Traversal

#2. Non-recursive using Stack

#3. Morris Traversal

#Approach1:Recursive

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def inOrder(root):               #LNR
            if not root:
                return 
            inOrder(root.left)
            ans.append(root.val)
            inOrder(root.left)
        inOrder(root) 
        return ans 


#Appraoch 2:Non-recursive/Iterative Approach using stack
#We can use a stack to perform the inorder traversal. We push the left nodes as many as possible to the stack, pop one, and then go to its right tree.
#TC:O(N) ,SC:O(N)

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root is None:
            return ans
        
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right
        return ans
