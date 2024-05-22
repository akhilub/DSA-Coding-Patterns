#Solution 1: BFS

#We use a queue q for level order traversal. Each time we traverse a level, we connect the nodes of the current level in order.

#The time complexity is O(n), and the space complexity is O(n). Here, n is the number of nodes in the binary tree.

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        
        q = deque([root])
        
        while q:
            prev =None
            for _ in range(len(q)):
                node = q.popleft()
                if prev:
                    prev.next = node
                prev = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root
