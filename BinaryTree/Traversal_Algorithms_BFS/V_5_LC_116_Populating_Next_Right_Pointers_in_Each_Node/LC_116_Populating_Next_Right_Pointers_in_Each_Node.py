# Approach 1: BFS

# Use a queue for level order traversal, and each time you traverse a level, connect the nodes of the current level in order.

# The time complexity is O(n), and the space complexity is O(n). Here, n is the number of nodes in the binary tree



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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        # q = deque(root) ===> TypeError: 'Node' object is not iterable
        # make it a list [], so it's iterable

        q = deque([root])

        while q:
            prev = None
            for _ in range(len(q)):
                node = q.popleft:
                
                #Connecting Nodes                                             
                if prev:                                    #For each node at the current level:
                    prev.next = node                        #If prev is not None, set prev.next to the current node, effectively linking the previous node to the current node.
                 prev = node                                #Update prev to the current node.
                    
                #Adding Children to Queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            return root


