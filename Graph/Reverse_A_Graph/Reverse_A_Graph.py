# ALGORITHM TO REVERSE A GRAPH (ADJACENCY LIST)
# A graph (noted as G(V, E) where V is set of vertices and E is set of edges) is a data structure that can be reprsented by Adjacency Matrix or Adjacency List. We can reverse a Graph by two steps. First, clone all the vertices and then iterate each edge in original Graph and add their reversed edges into the new Graph.

# The time and space complexity is O(VE).


#In simple term look adjacency list(graph) as list of list and we want to perform certain operations as per the output requirements
#For Graph represented via adjacency list i.e list of list index is the node/vertex and each list elements are the edges
from typing import List
class Solution:
    def reverseGraph(self, graph: List[List[int]]) -> List[List[int]]:
        rev = [[] for _ in range(len(graph))] #create the graph with just vertices

        for u,v in enumerate(graph):    #
            for k in v:                 # iterate over each edge
                rev[k].append(u)        # add reversed edge
        return rev



if __name__=="__main__":
    graph = [
        [1],
        [2],
        []
    ]

    expected_output = [
    [],
    [0],
    [1]
    ]

    sol = Solution()
    res = sol.reverseGraph(graph)
    print('reversed graph',res)


    graph2 = [
        [1,3],
        [2],
        [],
        [0]
    ]

    res2 = sol.reverseGraph(graph2)
    print('reversed graph',res2)
