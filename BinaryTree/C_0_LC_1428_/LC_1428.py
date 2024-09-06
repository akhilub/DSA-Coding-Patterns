#Approach:DFS (Recursion+Memoization)

# Definition for Node.
class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        def dfs(root):
            #Base/Terminal Cases
            if root is None:
                return None
            if root in nb:
                return nb[root]
            
            
            #Create newNode & register
            copy = NodeCopy(root.val)
            nb[root] = copy
            
            
            #Copy node properties into newNode properties
            copy.left = dfs(root.left)
            copy.right = dfs(root.right)
            copy.random = dfs(root.random)
            
            
            #return the newNode(aka cloned node)
            return copy

        
        nb = {}
        return dfs(root)