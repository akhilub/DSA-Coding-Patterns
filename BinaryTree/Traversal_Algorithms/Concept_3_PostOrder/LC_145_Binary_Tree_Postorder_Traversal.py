#Solutions
#1. Recusive Traversal

#2. Non-recursive using Stack

#3. Morris Traversal

#Appeoach1:Recursive

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def postorder(root):
            if root is None:
                return 
            postorder(root.left)
            postorder(root.right)
            ans.append(root.val)
            
        postorder(root)
        return ans


#Approach: Non-recursive/Iterative Using A Stack
#Reverse the solution we get from doing the reverse preorder traversal i.e. NRL (Node-Right-Left), no need for extra array.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans =[]
        if root is None:
            return ans
        stack = [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return ans[::-1]

            
            
