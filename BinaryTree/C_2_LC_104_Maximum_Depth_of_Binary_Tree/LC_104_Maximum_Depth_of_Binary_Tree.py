#Recursive Algorithm
#Approach: if the tree is None return 0, otherwise it will be the max of left the right tree respectively which we can recursively to get the value
#TC: O(N) where N is the number of nodes in BT
#SC: O(N) due to recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1+ max(left,right)


#Approach :BFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        q = deque([root])
        while q:
            ans+=1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans
        