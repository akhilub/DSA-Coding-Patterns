'''
Dijkstra Single Source Shortest Path Graph Algorithm
The Dijkstra Algorithm is the most famous Single Source Shortest Path (SSSP) Algorithm for a Weighted Graph with no negative weight. 
Dijkstra is optimal as the time complexity is O(E+VlogV). 
It is fast as it makes an assumption that the weights of the edges are positive.

The Dijkstra algorithm consists of two steps (and repeat it): Update the Estimates and then Pick the next vertex with the smallest cost in the unexplored set of vertices.

1. Update the Estimates: Dijkstra updates the shortest distance from the current vertex to all the neighbour vertices that it connects to. 
Initially, the cost to all the vertices in the Graph except the source is infinity.
2. Pick the next vertex from unexplored set of vertices. Once Dijkstra explores a vertex, it has the shortest path to it and assumes there is no shorter path by adding more edges with positive weights

Here is the Dijkstra algorithm in Python. Dijkstra has many variants and below is the classic one that is implemented using Priority Queue (or heap). 
Dijkstra is complete as one the queue is empty, it has all the shortest paths from the source to all other vertices. 
Uniform Cost Search (UCS) is a variant of Dijkstra and UCS is incomplete.
'''
from collections import defaultdict
from heapq import *
from math import inf

class Solution:
    def solve(self, edges , s , e):
        G = defaultdict(list)
        N = 0
        #o - origin , d - destination , w - weight
        for o , d , w in edges:     
            G[o]+=[(d,w)]
            N =max(N,o,d)
        N+=1
        
        return self.dijkstra(G, s, e) # Call dijkstra and return its result

    def dijkstra(self,G,s,e): 
        pq = [(0,s)]                    # starting priority with 0 weight and src node
        ans = defaultdict(lambda:inf)
        seen = set()
        while pq:
            w , v = heappop(pq)  # w-current weight/cost, v- current vertex
            
            if v in seen:
                continue
            seen.add(v)
            # ans[v]=w
            
            for nei_v,nei_w in G[v]:   #nei_v - neighbouring vertex , nei_w - neighboring weight
                if w + nei_w < ans[nei_v]:
                    ans[nei_v] = w + nei_w
                    heappush(pq, ( w + nei_w, nei_v))
                    
        # print(ans) 
        return ans[e] if ans[e]< inf else -1
        
        




if __name__=="__main__":
    sol = Solution()
    
    edges = [
    [0, 1, 3],
    [1, 2, 2],
    [0, 2, 9]]
    
    s = 0 
    e = 2
    actual_output = sol.solve(edges,s,e)
    print(actual_output)
    expected_output = 5
    print('Test Case Passed',actual_output==expected_output)
    
    
    
'''
Unlike Dijkstra, BFS (Breadth First Search) Algorithm is based on queue (First In First Out) and can only work in unweighted graphs (or graphs with equal weights). The time complexity for BFS is O(E+V) - Introduction to Dijkstra Single Source Shortest Path Graph Algorithm algorithms Dijkstra Shortest Path Graph Algorithm as in the worst case, the BFS needs to explore all the edges and vertices. BFS traverses the graph in level by level order. And Dijkstra can be categorized as “Best First Search” as it uses a heap or priority queue to extract the current “best” aka minimal cost from the queue.

The Floyd Warshal, on the other hand, is a multi source short path algorithm that runs in a much higher complexity O(V^3) time and O(V^2) space
'''