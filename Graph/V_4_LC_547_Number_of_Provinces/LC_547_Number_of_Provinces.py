#Approch :BFS

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def adj_list(grid):
            G=defaultdict(list)
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j]==1 and i!=j: #Exclude self loop           
                        G[i].append(j)
            return G

        G = adj_list(isConnected)
        print(G)


        def graph_bfs(source):
            q = deque([source])
            seen.add(source)
            while q:
                node = q.popleft()
                for neighbour in G[node]:
                    if neighbour not in seen:
                        seen.add(neighbour)
                        q.append(neighbour)
        
        ans = 0
        seen = set()
        
        for i in range(len(isConnected)):
            if i not in seen:
                graph_bfs(i)
                ans+=1
        
        return ans





















#Competative Programming

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i: int):
            vis[i] = True
            for j, x in enumerate(isConnected[i]):
                if not vis[j] and x:
                    dfs(j)

        n = len(isConnected)
        vis = [False] * n
        ans = 0
        for i in range(n):
            if not vis[i]:
                dfs(i)
                ans += 1
        return ans