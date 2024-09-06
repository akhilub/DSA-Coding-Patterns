#Approach:Recursion + Memomization
#TC:O(n)
#SC:O(n)
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head): # -> 'Node':
       
        # Helper function to recursively clone nodes
        def deepcopy(node):
            # Terminal Returns
            if not node:
                return
            if node in nb:
                return nb[node]
    
            # Create node and register it immediately (to break cycles)
            newNode = Node(node.val)
            nb[node] = newNode 
            
            # Fix Node Properties
            newNode.next   = deepcopy(node.next)
            newNode.random = deepcopy(node.random)
            
            return newNode
        
        nb = {}   # or defaultdict()            # Map to store original nodes to cloned nodes
        return deepcopy(head)
    
    
    
'''
newNode = Node(node.val)
nb[node] = newNode

        ||
        ||  equivalent
        ||
        
nb[node] = newNode = Node(node.val)

'''