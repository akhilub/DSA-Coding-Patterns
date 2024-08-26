#Approach1:HashSet
'''
We use a hash table vis to record all nodes on the path from node p to the root node. 
Then we start from node q and traverse towards the root node. If we encounter a node that exists in the hash table 
vis, then this node is the nearest common ancestor of p and q, and we can return it directly.

The time complexity is O(n), and the space complexity is O(n). Here, 
n is the number of nodes in the binary tree.

'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        vis = set()
        
        node = p
        while node:
            vis.add(node)
            node = node.parent
            
        node = q 
        while node not in vis:
            node = node.parent
        return node
            
            
        

#Approach2:Two Pointers

'''
We can use two pointers a and b to point to nodes p and q respectively, and then traverse towards the root node. 
When a and b meet, it is the nearest common ancestor of p and q. 
Otherwise, if pointer a traverses to the root node, then we let it point to node q, and do the same for pointer b. 
In this way, when the two pointers meet, it is the nearest common ancestor of p and q.

The time complexity is O(n), where n is the number of nodes in the binary tree. The space complexity is O(1).

'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        a , b = p, q 
        while a!=b:
            a = a.parent if a.parent else q 
            b = b.parent if b.parent else p 
        return a 
