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
        N = len(isConnected)
        for i in range(N):
            if i not in seen:
                graph_bfs(i)
                ans+=1
        
        return ans


#Another way of writing the above without converting the input,
#This works when input graph is represented in adjacency matrix form with 0 and 1 to indicate connectivity.

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
            def bfs(source):
                q = deque([source])
                seen.add(source)
                while q:
                    node = q.popleft()
                    for nei, adj in enumerate(isConnected[node]):
                        if adj and nei not in seen:
                            seen.add(nei)
                            q.append(nei)

            ans = 0
            seen = set()
            N = len(isConnected)
            for i in range(N):
                if i not in seen:
                    bfs(i)
                    ans += 1
            return ans


# Q) explain why you need adj and nei? and not just the nei?

# so 'adj' for connection and 'nei not in seen' for not visited/seen

# neigh is the index 0, 1, 2, 3, ...n
# adj is the value which is 0 or 1

# you only want to bfs when there is a connection (1), and keep track of "visited/seen" by the unique index



















#Competative Programming
#Approach:DFS Recursive

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


