#Approach : BFS on a grid
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        minutes = 0 #ans 
        fresh_oranges_count = 0
        q = deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c]==2: #found a rotten orange 
                    q.append((r,c)) # add the cell to the queue
                elif grid[r][c]==1: #found a fresh orange
                    fresh_oranges_count+=1 #increment the count of fresh oranges by 1
        
        
        while q and fresh_oranges_count: #while q is not None and fresh_oranges_count is not 0
            
            minutes+=1
            q_size = len(q) #Process all the oranges in the current minute
            
            for _ in range(q_size):
                i , j = q.popleft()
                
                for di,dj in directions:# Check all the neighboring positions
                    nr ,nc= i+di,j+dj
                    
                    if 0<=nr<m and 0<=nc<n: # If the neighbor is within the grid 
                        if grid[nr][nc]==1:
                            fresh_oranges_count-=1 #decrement the count of fresh oranges
                            grid[nr][nc]=2 # make the fresh orange rotten
                            q.append((nr,nc)) #add fresh orange to be processed in queue
                                       
        return minutes if fresh_oranges_count == 0 else -1