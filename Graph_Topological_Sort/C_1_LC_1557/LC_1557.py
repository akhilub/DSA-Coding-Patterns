# Time: O(∣E∣) ,E - no of edges
# Space: O(|V|) , V - no of vertices/nodes

# Approach:Topological Sort,
# Variation: When `n` is not given
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        inDegrees = defaultdict(int)
        nodes = set()
        for s , e in edges:
            inDegrees[e]+=1
            nodes.add(s)
            nodes.add(v)
        
        ans = []
        for N in nodes:
            if inDegrees[N]==0:
                ans.append(N)
        return ans


#Another Way of writing,utilizing given 'n'
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        inDegrees = [0]*n

        for _, v in edges:
            inDegrees[v]+=1
            
        return [i for i , d in enumerate(inDegrees) if d==0]
    
    
#Approach 2:Optimised/Using In-Built HashMap

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        cnt = Counter(t for _, t in edges)  #inDegrees HashMap
        return [i for i in range(n) if cnt[i] == 0]
    

    
    
    
    