from typing import Dict, List
from collections import defaultdict
from heapq import *
from math import inf

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        #Created Adjacency list Graph
        G = defaultdict(list)
        # o - origin, d - dst, w-weight
        for o , d , w in edges:
            G[o]+=[(d,w)]
        print(G)
        
        #Dijktras
        ans = defaultdict(lambda:inf)
        # print(ans[100])
        pq = [(0,src)]
        seen = set()
        
        while pq:
            w , v = heappop(pq) # w - current weight/cost , v - current vertex
            if v in seen:
                continue
            
            seen.add(v)
            ans[v]= w
            
            for nei_v,nei_w in G[v]:  #nei_v - neighbouring vertex , nei_w - neighboring weight 
                if w+nei_w < ans[nei_v]:  #check weight condition 
                    ans[nei_v] = w+nei_w
                    heappush(pq , [w+nei_w,nei_v])
        
        for node in range(n):
            if node not in ans:
                ans[node] = -1
        return ans
        
        
            
if __name__=="__main__":
    sol = Solution()
    n = 5
    edges = [[0,1,10], [0,2,3], [1,3,2], [2,1,4], [2,3,8], [2,4,2], [3,4,5]]
    src = 0
    
    actual_output = sol.shortestPath(n,edges,src)
    print(actual_output)
    expected_output = {0:0, 1:7, 2:3, 3:9, 4:5}
    print('Test Case Passed',actual_output==expected_output)