#Logic
#Key thing to remember is Given graph is DAG so backtracking template will work

'''
Since the Graph is DAG (Directed Acyclic Graph), it does not have cycles. We then can simplify the implementation without needing to use a `set` to avoid the nodes that we have visisted. We can perform a Depth First Search Algorithm and keep tracking a current path which will be added to the result once we reach the destination.

The space complexity is also O(N) - if we ignore the space required to store all paths (which is N*2^N) as we are using Recursion and need to have a current path list. The time complexity in worst case is O(N*2^N) if each node can be connected to the nodes that have greater values. For example, 0 to 1..n, 1 to 2..n, 3 to 4..n.
'''

#Write this in interviews 
#Approach:DFS (I prefer this, this DFS is optimised)
#Time:O(n•2ⁿ)
#Space:O(n•2ⁿ)

'''
Ctrl+Cmd+Space -> brings up character selector in mac to choose superscript or subscript
'''


class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        ans = []
        def dfs(u:int, path:List[List[int]]):
            if u == len(graph)-1:
                ans.append(path[:])
                return
            
            for v in graph[u]:      #v-nextNode, u-currentNode
                dfs(v,path+[v])

        dfs(0,[0]) #starting the search from source node/level `0` , with path source `[0]`
        return ans





#Approach:BFS Optimised
class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        ans = []
        q = deque([[0]])            # q = deque([[source]]) -> adding starting path with source `[source]`; basically a list with element in deque
        while q:
            path = q.popleft()      #path - currentPath
            u = path[-1]            #u -currentNode

            if u == len(graph)-1:
                ans.append(path)
                continue
            
            for v in graph[u]:      #v -nextNode
                q.append(path+[v])  #Critical step 
                
        return ans























#Finding All Paths from Source to Target in a Directed Acyclic Graph (DAG) using Breadth First Search Algorithm
'''
Breadth First Search Algorithm can be used to traverse a Graph. 
We keep tracking of the current Node and the path followed so far. 
The graph is DAG – hence there isn’t cycles and we don’t need to manually avoid re-visiting same nodes.

Each node in the worst case, connects to other greater nodes. 
The total paths could be 2^(N-1)-1. Considering O(N) time to build a path, total complexity is O(N*2^N). 
The space complexity is O(N*2^N+N) if we are considering the space to store all the paths. 
Otherwise, the space complexity is O(N) for a de-queue.
'''


#My Full Approach,Good for understanding graph traversals
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #Create Graph basically mapping list indices to its values in a dictionary/hashtable
        G = defaultdict()
        for i in range(len(graph)):
            G[i] = graph[i]
            
        
        #Defining Variables
        n = len(graph)
        src ,dst = 0 , n-1
        
        
        #Apply BFS
        ans = []                     #collecting all path from source to dst
        q = deque([(src, [src] )])
        while q:
            
            node, path = q.popleft() #node - currentNode , path-currentPath
            if node==dst:
                ans.append(path)
            
            for nei in G[node]:      #nei aka neighbor - nextNode
                q.append(( nei, path+[nei] ))
                    
        return ans    