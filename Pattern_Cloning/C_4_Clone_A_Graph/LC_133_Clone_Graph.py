#Approach:DFS (Recursion+Memomization)
#TC:O(n)
#SC:O(n)
#Write this in interviews

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def dfs(node,nb = {}):
            if node is None:
                return None
            if node in nb:
                return nb[node]
            
            nb[node] = newNode = Node(node.val)
            
            newNode.neighbors = [dfs(neibor) for neibor in node.neighbors]
            
            return newNode
        
        return dfs(node)
    

#Same Above Approach in expanded form
class Solution: 
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        def clone(node):
            if not node: 
                return None
            if node in nb: 
                return nb[node]
            
            cloneNode = Node(node.val)
            nb[node] = cloneNode
            
            for neighbor in node.neighbors:
                cloneNode.neighbors.append(clone(neighbor))
            
            return cloneNode
        
        nb= defaultdict()
        return clone(node)
    
    














#Approach : BFS Graph Traversal 
#Data Structure : HashMap 

# CLONE A GRAPH USING BREADTH FIRST SEARCH ALGORITHM
# A Graph is a collections of vertices and edges and can be noted G = (V,E) 


# we can use Breadth First Search Algorithm to traverse a Graph. And we can clone/copy a Node while we are visiting a Node in the first time, 
#and also we need to copy the edge i.e. add the neighbour nodes to the current nodes’ neighbour list.

# We use a queue to implement a Breadth First Search Algorithm.

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        q = deque([node])
        seen = {}
        seen[node] = Node(node.val,[])
        while q:
            curNode = q.popleft()
            for nei in curNode.neighbors:
                if nei not in seen:
                    seen[nei] = Node(nei.val,[])
                    q.append(nei)
                seen[curNode].neighbors.append(seen[nei])

        return seen[node]

# The time complexity is O(N+M) where N is the number of the vertices in the Graph, and M is the number of the edges.
# The space complexity is O(N) as we are using a queue to store the graph vertices/nodes.
                








