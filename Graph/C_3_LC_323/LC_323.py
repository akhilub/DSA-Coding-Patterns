#Approach: BFS


# One solution is to use BFS. The idea is to give each node a flag to mark whether it has been visited. 
#For an unvisited node, we will increment the result `ans` by 1, because this must be a new connected region., And then we traverse the neighboring nodes through the adjacency list and mark them as visited.

# After traversing all connected nodes, we continue to look for the next unvisited node, and so on until all nodes have been visited, then the number of connected regions is also calculated at this time





from collections import defaultdict, deque

class Solution:
    def countComponents(self, n, edges):
        # Create a graph as an adjacency list
        G = defaultdict(list)
        for s, e in edges:
            G[s].append(e)
            G[e].append(s)

        def bfs(source):
            # Initialize a queue with the source node
            q = deque([source])
            # Add the source node to the seen set
            seen.add(source)
            while q:
                node = q.popleft()
                # Traverse all the neighbors of the current node
                for neighbor in G[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        q.append(neighbor)

        ans = 0 
        seen = set()
        # Iterate through each node
        for i in range(n):
            if i not in seen:
                # If the node is not seen, it means we have found a new connected component
                bfs(i)
                ans += 1

        return ans
