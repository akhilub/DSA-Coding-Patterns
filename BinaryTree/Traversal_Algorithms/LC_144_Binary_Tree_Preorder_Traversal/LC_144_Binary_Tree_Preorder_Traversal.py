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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def preorder(root):
            if root is None:
                return 
            ans.append(root.val)
            preorder(root.left)
            postorder(root.right)
        preorder(root)
        return ans

#Approach2: Non-recursive/Iterative Using Stack
#1)Write BFS traversal using queue DS(deque)
#2)Replace queue with stack DS(list) ,we get reverse pre-order traversal algorithm i.e. NRL (Node-Right-Left):
#3)As the stack push/pop gives the reverse order, we can swap around the pushing of left and right nodes, that is, push the right nodes and then left node, this will give the Preorder Traversal Algorithm.
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans

        stack = [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)                        #here the order matters in when we pop element from stack in order of NLR
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ans 

