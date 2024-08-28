#Minimum Starting Nodes to Visit Graph (Topological Sort, Indegree)
'''
We can iterate over the edges and update the indegree for each vertex. 
The indegree is the number of edges that point to a vertex while the outdegree is the number of edges that go out from a vertex.

Then, we can iterate over all vertices and store the answer as those whose indegree is zero
'''
#This is the fundamental of a Topological Sorting on a Graph. Time and space complexity is O(N+M) where N is the number of edges and M is the number of vertices in the given Graph

from collections import defaultdict
from typing import List
class Solution:
    def minimumStartingNodes(self,edges:List[List[int]])->List[int]:
        inDegrees = defaultdict(int)
        nodes = set()
        for u , v in edges:
            inDegrees[v]+=1
            nodes.add(u)
            nodes.add(v)
        
        ans = []
        for N in nodes:     #N-node
            if inDegrees[N]==0:
                ans.append(N)
        
        return ans
            
        
if __name__=="__main__":
    edges1 = [[0,1],[1,2],[3,2]]
    expected_output= [0,3]
    
    actual_output = Solution().minimumStartingNodes(edges1)
    print('TestCase1 Passed',actual_output==expected_output)

    edges2 = [[1,0],[2,0],[3,2],[4,3]]
    expected_output = [1,4]
    
    actual_output = Solution().minimumStartingNodes(edges2)
    print('TestCase2 Passed',actual_output==expected_output)
    
    