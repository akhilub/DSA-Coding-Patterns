#Multisource BFS: Approach on how to start think for BFS + Bitmasking

class Solution:
  def shortestPathLength(self, graph: list[list[int]]) -> int:
    n = len(graph)
    goal = (1 << n) - 1 # 1<<n is equal to 2^n , idea is to explore all possible combinations/paths

    ans = 0
    q = collections.deque()  # (u, state)
    seen = set()

    for i in range(n):
      q.append((i, 1 << i))

    while q:
      for _ in range(len(q)):
        u, state = q.popleft()
        
        if state == goal:
          return ans
        
        if (u, state) in seen:
          continue
        seen.add((u, state))
        for v in graph[u]:
          q.append((v, state | (1 << v)))
    
      ans += 1

    return -1













#Concised above code only

#Approach : BFS + BitMasking

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        # BFS queue: (distance, node, visited_nodes_bitmask)
        queue = deque([(0, i, 1 << i) for i in range(n)])
        visited = {(i, 1 << i) for i in range(n)}

        while queue:
            dist, node, bitmask = queue.popleft()

            # If all nodes have been visited, return the distance
            if bitmask == (1 << n) - 1:
                return dist

            # Traverse neighbors
            for neighbor in graph[node]:
                new_bitmask = bitmask | (1 << neighbor)
                if (neighbor, new_bitmask) not in visited:
                    visited.add((neighbor, new_bitmask))
                    queue.append((dist + 1, neighbor, new_bitmask))

        return -1  # Should never reach here if the graph is connected