#Note: Dont go for DFS Stick to BFS 
#Interviewers do not want you to modify the input array
#Stick to BFS for interviews

#Input modification is not allowed
#BFS Algorithm
from collections import deque
class Solution:
    def numIslands(self,grid:List[List[str]])-> int:
        rows =len(grid)
        cols = len(grid[0])
        visited = set()
        totalIslands =0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def bfs(i,j):
            q = deque([(i,j)]) #add in the queue to process
            visited.add((i,j)) #mark the cell as visited
            while q:
                row,col = q.popleft()
                for di,dj in directions: #explore the directions
                    nr = row + di
                    nc = col + dj
                    if 0<=nr<rows and 0<=nc<cols:# within the boundaries
                        if grid[nr][nc]=="1" and (nr,nc) not in visited: #check if its a land and is not visited then add it to queue and mark it as visited
                            q.append((nr,nc))
                            visited.add((nr,nc))
        
        for r in range(rows):        
            for c in range(cols):      
                if grid[r][c]=="1" and (r,c) not in visited:
                    bfs(r,c)
                    totalIslands+=1

        return totalIslands






#When input modification is allowed
#DFS Algorithm 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        totalIslands = 0

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols:  #check if current cell is out of bounds 
                return
            
            if grid[r][c] !="1":  #not land ,could be water(0) or visted land(v)
                return
            
            grid[r][c]="v"  #mark current land as visited
            
            #explore the neighbour
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        #Iterate through all cells in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":    #found land
                    dfs(r,c)
                    totalIslands+=1
        
        return totalIslands