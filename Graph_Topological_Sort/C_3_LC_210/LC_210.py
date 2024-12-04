# Approach:Topological Sorting
# Time: O(∣V∣+∣E∣), ∣V∣=numCourses and ∣E∣=∣prerequisites∣
# Space: O(∣V∣+∣E∣), where ∣V∣=numCourses and ∣E∣=∣prerequisites∣

class Node(object):
    def __init__(self):
        self.inDegrees = 0
        self.outNodes = []
        
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        G = defaultdict(Node)
        
        # Create graph
        for s, e in prerequisites:  # s - start, e - end
            G[s].inDegrees += 1
            G[e].outNodes.append(s)
        
        # Initialize queue with courses that have zero in-degrees
        q = deque()
        for i in range(numCourses):
            if G[i].inDegrees == 0:
                q.append(i)
                
        ans = []
        while q:
            v = q.popleft()  # v - current vertex
            ans.append(v)
            for a in G[v].outNodes:
                G[a].inDegrees -= 1
                if G[a].inDegrees == 0:
                    q.append(a)
        
        return ans if len(ans) == numCourses else []
    
    


#Another Condensed Way of Writing the above
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        indeg = [0] * numCourses
        for a, b in prerequisites:
            g[b].append(a)
            indeg[a] += 1
        ans = []
        q = deque(i for i, x in enumerate(indeg) if x == 0)
        while q:
            i = q.popleft()
            ans.append(i)
            for j in g[i]:
                indeg[j] -= 1
                if indeg[j] == 0:
                    q.append(j)
        return ans if len(ans) == numCourses else []
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#Approach DFS

    
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        #Create adjacency List
        G = [[] for _ in range(numCourses)]
        for course , prereq in prerequisites:
            G[course].append(prereq)
        
        #Track visited course and current path 
        vis = set()
        path = set()
        
        
        def dfs(course):
        #If course is in path, we found a cycle
            if course in path:
                return
        
        #If course is already visited,its safe
            if course in vis:
                return True
        #Add course to current path
            path.add(course)

        # Check all prerequisite
            for prereq in G[course]:
                if not dfs(prereq):
                    return False 
        
        # Remove course from current path
            path.remove(course)
            
        # no cycle found, dfs finished, good to add the course into the ans
            ans.append(course)
            
        # Mark course as visited
            vis.add(course)
            
        
            return True
        
        
        
        #Check all courses
        ans =[]
        for course in range(numCourses):
            if not dfs(course):
                return []
            
        return ans