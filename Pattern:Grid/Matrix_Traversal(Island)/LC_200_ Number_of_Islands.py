#Note: Dont go for DFS Stick to BFS 

#Input modification is not allowed
#BFS Algorithm
#Stick to BFS for interviews
from collections import deque
class Solution:
    def numIslands(self,grid:List[List[str]])-> int:
        rows =len(grid)
        cols = len(grid[0])
        visited = set()
        totalIslands =0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def bfs(i,j):
            q = deque([(i,j)])
            visited.add((i,j))
            while q:
                row,col = q.popleft()
                for di,dj in directions:
                    nr = row + di
                    nc = col + dj
                    if 0<=nr<rows and 0<=nc<cols:
                        if grid[nr][nc]=="1" and (nr,nc) not in visited:
                            q.append((nr,nc))
                            visited.add((nr,nc))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    bfs(r,c)
                    totalIslands+=1

        return totalIslands





#Interviewers do not want you to modify the input array
#When input modification is allowed
#DFS Algorithm 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        totalIslands = 0

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols:  #out of bounds 
                return
            
            if grid[r][c] !="1":  #not land ,could be water(0) or visted land(v)
                return
            
            grid[r][c]="v"  #mark land as visited
            
            #explore the neighbour
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":    #found land
                    dfs(r,c)
                    totalIslands+=1
        
        return totalIslands