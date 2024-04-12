# Approach: 
# We will traverse the grid linearly
# Whenever we find the land cell (with value 1) we have found a island.Using that cell as the root node we will perform DFS or BFS to find its all connected land
# During DFS or BFS we will explore the cell neighours in 4 directions (horizontslly and vertically) to find and mark the connected land cells.
# We will keep a variable to remember the area of the islands
# Finally Out of all the islands we will return the maxArea one

#DFS 
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows =len(grid)
        cols = len(grid[0])
        maxAreaIsland = 0
        
        #dfs function will give us the area of island
        def dfs(r,c):
            if r< 0 or r >=rows or c<0 or c >=cols: #out of bound
                return 0
            
            if grid[r][c]!=1: #not land, could be water (0) or visited land(v)
                return 0
            
            grid[r][c] = 'v' #mark land as visited
            
            area = 1 # counting the cell
            area +=dfs(r+1,c)
            area +=dfs(r-1,c)
            area +=dfs(r,c+1)
            area +=dfs(r,c-1)
            
            return area
            
        
        #Grid Traversal to find the land cell
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    maxAreaIsland = max(maxAreaIsland ,dfs(r,c))
        
        return maxAreaIsland

#Approach: 
#BFS using queue
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        maxAreaIsland = 0
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        
        #bfs function will give us the area of island
        def bfs(r,c):
            q=deque([(r,c)])
            visited.add((r,c)) # mark the cell as visited by adding it to set
            area = 1 #counting the cell
            while q:
                row,col = q.popleft()
                #exploring the neighbor
                for dr,dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if 0<=nr<rows and 0<=nc<cols:
                        if grid[nr][nc]==1 and (nr,nc) not in visited:
                            q.append((nr,nc))
                            visited.add((nr,nc))
                            area+=1
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visited:
                    maxAreaIsland = max(maxAreaIsland,bfs(r,c))
                    
        return maxAreaIsland

                    