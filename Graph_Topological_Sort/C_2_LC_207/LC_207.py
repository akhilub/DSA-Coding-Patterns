# Approach:Topological Sorting using BFS

# Time: O(∣V∣+∣E∣), ∣V∣=numCourses and ∣E∣=∣prerequisites∣
# Space: O(∣V∣+∣E∣), where ∣V∣=numCourses and ∣E∣=∣prerequisites∣

'''
Topological Sorting
For this problem, we can consider the courses as nodes in a graph, and prerequisites as edges in the graph. 
Thus, we can transform this problem into determining whether there is a cycle in the directed graph.

Specifically, we can use the idea of topological sorting. 
For each node with an in-degree of 0, we reduce the in-degree of its out-degree nodes by 
1, until all nodes have been traversed.

If all nodes have been traversed, it means there is no cycle in the graph, and we can complete all courses; otherwise, we cannot complete all courses.

The time complexity is O(n+m), and the space complexity is O(n+m). Here, n and m are the number of courses and prerequisites respectively.
'''

#Topological Sort Algorithm on Directed Graphs – via BFS
#The Topological sorting gives an order that we can visit the vertices in a directed graphs where the prerequisite vertices need to be visited first. 
# A prerequisite or dependency is a edge with direction. We can first start with all nodes that have zero indegree (meaning no edges coming to them) – and then we can decrement the indegree of all out nodes as we deque a current vertex. 
# Once a out node has become zero indegree, we can visit it – thus pushing to the queue.


class Node(object):
    def __init__(self):
        self.inDegrees = 0
        self.outNodes = []
 
class Solution(object):
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ## Build the graph.
        G = defaultdict(Node)
        for a, b in prerequisites:  # a-start , b-end of edges aka prerequisites
            G[a].inDegrees += 1
            G[b].outNodes.append(a)
        
        # Initialize queue with courses that have zero in-degrees    
        q = deque()             
        for i in range(numCourses):
            if G[i].inDegrees == 0:
                q.append(i)
        
        #Perform topological sorting.
        
        #Apply BFS on Graph         
        cnt = 0
        while q:
            v = q.popleft()     #v - current vertex
            cnt+=1
            for a in G[v].outNodes:
                G[a].inDegrees -= 1
                if G[a].inDegrees == 0:
                    q.append(a)
                    
        return cnt==numCourses
    
#When the queue is exited (the BFS terminates), if the number of indegrees we decrement is not equal to the number of edges, thus there is a Cycle in the Graph – hence we cannot visit all the nodes.



#Another Condensed Way of Writing

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        indeg = [0] * numCourses
        for a, b in prerequisites:
            g[b].append(a)
            indeg[a] += 1
        
        cnt = 0
        q = deque(i for i, x in enumerate(indeg) if x == 0)
        while q:
            i = q.popleft()             # i-current node 
            cnt += 1
            for j in g[i]:              # j-neighbours
                indeg[j] -= 1
                if indeg[j] == 0:
                    q.append(j)
        return cnt == numCourses