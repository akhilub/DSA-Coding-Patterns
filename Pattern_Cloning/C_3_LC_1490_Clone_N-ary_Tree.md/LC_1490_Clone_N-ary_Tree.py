#Approach:Recursion+Memoization
# Time:  O(n)
# Space: O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""


class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        def deepCopy(node):
            if node is None:
                return
            if node in nb:
                return nb[node]
            
            
            nb[node] = newNode = Node(node.val)
            
            newNode.children = [deepCopy(c) for c in node.children]

            return newNode                
        
        nb=defaultdict()        #dict()
        return deepCopy(root)
    
    



#Solution

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        children = [self.cloneTree(child) for child in root.children]
        return Node(root.val, children)