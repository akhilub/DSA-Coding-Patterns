#GRAPH ALGORITHM: BREADTH FIRST SEARCH TO CHECK CONNECTIVITY BETWEEN VERTICES
#We can use the Breadth First Search Algorithm (BFS) to traverse a Graph just like we use it on a Tree. We need a hash set to remember the vertices that we have visited so that we don’t repeatedly expand them in BFS (cycles).

#We can store the Graph using Adjacent List – each vertex points to a list of vertices that it links to.

# The time and space complexity are both O(N) where N are the vertices in the Graph.

from collections import deque,defaultdict
from typing import List
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        #Convert input into equivalent adjacency list
        G = defaultdict(list[int])
        for s,e in edges:
            G[s].append(e)
            G[e].append(s)

        #Apply graph bfs
        q = deque([source])
        seen = {source}
        while q:
            node = q.popleft()
            if node == destination:       
                return True
            for neighbour in G[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    q.append(neighbour)

        return False


'''
seen = {source}
...
...
    for neighbour in G[node]:
        if neighbour not in seen:
            seen.add(neighbour)
            q.append(neighbour)

'''

#equivalent 

'''

seen =set()
...
...
    if node in seen:
        continue
    seen.add(node)
    for neighbour in G[node]:
        q.append(node)

'''