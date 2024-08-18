#Approach 1:BFS

# We can use the BFS method to solve this problem. First, enqueue the root node, then continuously perform the following operations until the queue is empty:
# Traverse all nodes in the current queue, store their values in a temporary array `t`, and then enqueue their child nodes.
# Store the temporary array `t` in the answer `ans` array.
# Finally, return the answer `ans` array.

# The time complexity is O(n) and the space complexity is O(n).Here, n is the number of nodes in the binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans =[]
        if root is None:
            return ans
        q = deque([root])
        while q:
            t = []                      #t-traversal order
            for _ in range(len(q)):
                node = q.popleft()
                t.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(t)
        return ans

