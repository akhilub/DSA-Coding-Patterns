#Points to remember 

# A tree is a special undirected graph. It satisfies two properties
# 1) It is connected
# 2) It has no cycle

#Approach
# Condition 1:Being connected means you can start from any node and reach any other node. To prove it, we can do a BFS and add each node we visit to a set. After we visited all the nodes, we compare the number of nodes in the set with the total number of nodes. If they are the same then every node is accessible from any other node and the graph is connected.

#Condition 2: no cycle can be expressed as No. of nodes == No of edges + 1.


#OR

#a graph is a tree when there are no self-loops or repeated edges
#Any tree (be it binary or not) with n nodes has n-1 edges otherwise there will be a cycle

# If we observe carefully the definition of tree and its structure we will deduce that if a graph is connected and has n – 1 edges exactly then the graph is a tree.
# Proof: 
# Since we have assumed our graph of n nodes to be connected, it must have at least n – 1 edges inside it. Now if we try to add one more edge than the n – 1 edges already the graph will end up forming a cycle and thus will not satisfy the definition of tree. Therefore, it is necessary for a connected graph to have exactly n – 1 edges to avoid forming cycle. 

#OR

# A graph qualifies as a valid tree if it meets the following criteria:
# 1)It is fully connected.
# 2)It has no cycles.



from collections import deque,defaultdict
from typing import List
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:        #An empty tree is a valid tree
            return True

        #Build Graph/Convert input to graph adjacency list 
        G = defaultdict(list[int])
        for s,e in edges:
            G[s].append(e)
            G[e].append(s)
        
        print(G)

        #Apply Graph BFS
        q = deque([0])
        seen = {0}
        while q:
            node = q.popleft()
            for neighbour in G[node]:
                if neighbour not in seen:
                    seen.add(neighbour)
                    q.append(neighbour)

        # print(seen)
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

