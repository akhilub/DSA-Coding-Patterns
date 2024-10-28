#Points to remember 

# A tree is a special undirected graph. It satisfies two properties
# 1) It is connected
# 2) It has no cycle


#OR


#a graph is a tree when there are no self-loops or repeated edges
#Any tree (be it binary or not) with n nodes has n-1 edges otherwise there will be a cycle

# If we observe carefully the definition of tree and its structure we will deduce that if a graph is connected and has n – 1 edges exactly then the graph is a tree.
# Proof: 
# Since we have assumed our graph of n nodes to be connected, it must have at least n – 1 edges inside it. Now if we try to add one more edge than the n – 1 edges already the graph will end up forming a cycle and thus will not satisfy the definition of tree. 
# Therefore, it is necessary for a connected graph to have exactly n – 1 edges to avoid forming cycle. 


#OR


# A graph qualifies as a valid tree if it meets the following criteria:
# 1)It is fully connected.
# 2)It has no cycles.
















#Approach1:Union-Find

'''
To determine whether it is a tree, the following two conditions must be met:

1.The number of edges is equal to the number of nodes minus one;
2.There is no cycle.

We can use a union-find set to determine whether there is a cycle. We traverse the edges, if two nodes are already in the same set, it means there is a cycle. Otherwise, we merge the two nodes into the same set. Then we decrease the number of connected components by one, and finally check whether the number of connected components is 1.

The time complexity is O(n×logn), and the space complexity is O(n), where n is the number of nodes.
'''

from typing import List
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Helper function to find root parent
        def find(x: int) -> int:
            if p[x] != x:
                p[x] = find(p[x])  # Path compression
            return p[x]
        
        
        p = list(range(n))      # Initialize parent array for each node
        for a, b in edges:
            pa, pb = find(a), find(b)  # Find root parents

            if pa == pb:        # Cycle detected
                return False
            p[pa] = pb          # Union nodes
            n -= 1  # Decrease count of components
            
        return n == 1  # Valid tree if exactly one component remains
    
    
    



#Approach:DFS
# Time: O(n)
# Space: O(n)

'''
We can also use depth-first search to determine whether there is a cycle. We can use a set `vis` to record the visited nodes. 
During the search, we first mark the node as visited, then traverse the nodes adjacent to this node. 
If the adjacent node has been visited, we skip it, otherwise we recursively visit the adjacent node. 
Finally, we check whether all nodes have been visited. 
If there are nodes that have not been visited, it means that it cannot form a tree, so we return false.

The time complexity is O(n), and the space complexity is O(n), where 
n is the number of nodes.
'''
    


class SolutionDFS:
    def validTreeDFS(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        
        G = [[] for _ in range(n)]
        for s,e in edges:
            G[s].append(e)
            G[e].append(s)
            

        def dfs(node:int):
            vis.add(node)
            for nei in G[node]:
                if nei not in vis:
                    dfs(nei)
            
        vis = set()
        dfs(0)
        return len(vis)==n





#Approach:BFS
# Time : O(n)
# Space: O(n)
from collections import deque
class SolutionBFS:
    def validTreeBFS(self, n: int, edges: list[list[int]]) -> bool:  
        #No cycle Condition
        if len(edges)!=n-1:
            return False
      
        #Build Graph: Here node is index value and neighbors are list value at each index
        G = [[] for _ in range(n)]
        for s,e in edges:
            G[s].append(e)
            G[e].append(s)
        
        #Apply BFS
        q = deque([0])
        seen = {0}
        while q:
            node = q.popleft()
            for nei in G[node]:
                if nei not in seen:
                    q.append(nei)
                    seen.add(nei)
                    
                  
        return len(seen)==n 





if __name__ == "__main__":
    n = 5
    edges = [[0,1],[0,2],[0,3],[1,4]]
    print(Solution().validTree(n,edges))
    print(SolutionDFS().validTreeDFS(n,edges))
    print(SolutionBFS().validTreeBFS(n,edges))
    
    n = 5 
    edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
    print(Solution().validTree(n,edges))
    print(SolutionDFS().validTreeDFS(n,edges))
    print(SolutionBFS().validTreeBFS(n,edges))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# Algorithm
# Condition 1:Being connected means you can start from any node and reach any other node.
 
# To prove it, we can do a BFS and add each node we visit to a set. 
# After we visited all the nodes, we compare the number of nodes in the set with the total number of nodes. 
# If they are the same then every node is accessible from any other node and the graph is connected.

# Condition 2: no cycle can be expressed as No. of nodes == No of edges + 1.
    
    
    
    



#Another way of writing BFS
from collections import deque,defaultdict
from typing import List
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:        #An empty tree is a valid tree
            return True

        #1.Build Graph/Convert input to graph adjacency list 
        G = defaultdict(list[int])
        for s,e in edges:
            G[s].append(e)
            G[e].append(s)
        
        print(G)

        #2.Apply Graph BFS, traverse the graph and store the nodes in a set
        q = deque([0])
        seen = {0}
        while q:
            node = q.popleft()
            for neighbour in G[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    q.append(neighbour)

        # print(seen)
        
        #3.Finally check if two conditions above are met
        return len(seen)==n and len(edges) == n - 1 #Checking for both conditions


if __name__=="__main__":
    n = 5 
    edges = [[0,1],[0,2],[0,3],[1,4]]
    expected_output = True

    sol = Solution()
    res1 = sol.validTree(n,edges)
    print('test case 1',res1)


    n = 5 
    edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
    expected_output = False

    res2 = sol.validTree(n,edges)
    print('test case 2',res2)
    
    
    n = 0 
    edges = [[]]
    expected_output = True

    res3 = sol.validTree(n,edges)
    print('test case 3',res3)

