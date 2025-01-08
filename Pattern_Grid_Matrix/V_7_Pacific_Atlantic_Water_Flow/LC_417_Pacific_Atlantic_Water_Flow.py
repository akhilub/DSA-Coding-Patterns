# 𝗚𝗿𝗮𝗽𝗵 𝗖𝗵𝗲𝗮𝘁 𝗦𝗵𝗲𝗲𝘁 - 𝗠𝗮𝘁𝗿𝗶𝘅 𝗗𝗙𝗦 𝗕𝗮𝗰𝗸𝘁𝗿𝗮𝗰𝗸𝗶𝗻𝗴

'''
DFS is a common graph traversal algorithm. In a matrix, we can use it to move in all four directions (up, down, left, right) and count the number of unique paths from the top-left cell to the bottom-right cell.

The below algorithm shows the process of finding a unique path using DFS.

𝗜𝗺𝗽𝗹𝗲𝗺𝗲𝗻𝘁𝗮𝘁𝗶𝗼𝗻

1. Use a hash set to track visited coordinates.
2. Add the current cell to the hash set and initialize count as 0.
3. Recursively perform DFS in all four directions.
4. If we go out of bounds, or a cell has already been visited or is blocked (1), no path exists: return 0.
5. If we are at the bottom right cell, we have reached the destination: return 1 and increment count.
6. After exploring all four directions of a cell, remove the cell's coordinates from the hash set to backtrack and explore other unique paths.
7. Finally, return the total number of unique paths found from all four directions.


𝗧𝗶𝗺𝗲 𝗮𝗻𝗱 𝗦𝗽𝗮𝗰𝗲

Time: O(4^n.m), in the worst case, each cell can have four recursive calls
Space: O(n.m), where n represents number of rows and m represents the number of columns

'''
#Approach: DFS (Using Set)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)            # m - rows
        n  = len(heights[0])        # n - cols
        
        # Hashset to track visited cordinates
        visP = set()                                                                                                           
        visA = set()                                                                                                           
        
        
        def dfs(i,j,h,vis):                                                                                   
            #(i,j) -current corrdinates , h - current cell height, vis - current set(ocean) 
            if i<0 or i>=m or j<0 or j>=n:              #Out of bounds
                return
            
            if (i,j) in vis or heights[i][j]<h:         #Question conditions not satisfied then return                              
                return             
            
            vis.add((i,j))                              #Add current cell to as visited  
                                 
            #Recursively perform DFS in all four directions.
            dfs(i+1,j,heights[i][j],vis)
            dfs(i-1,j,heights[i][j],vis)
            dfs(i,j-1,heights[i][j],vis)
            dfs(i,j+1,heights[i][j],vis)
            
        for r in range(m):
            """
            Perform DFS from cells on the left and right columns to explore cells reachable from the Pacific and Atlantic oceans, respectively.
            """
            dfs(r,0,0,visP)     #left edge
            dfs(r,n-1,0,visA)   #right edge
            
        for c in range(n):
            """
            Perform DFS from cells on the top and bottom rows to explore cells reachable from the Pacific and Atlantic oceans, respectively.
            """
            dfs(0,c,0,visP)     #top -edge
            dfs(m-1,c,0,visA)   #bottom - edge
        
        # Find cells reachable from both oceans.
        return [(i,j) for i in range(m) for j in range(n) if (i,j) in visP and (i,j) in visA]    





'''
for r in range(m):
    dfs(r,0,0,visP)
    dfs(r,n-1,0,visA)   
            
for c in range(n):
    dfs(0,c,0,visP)
    dfs(m-1,c,0,visA)

        
        ||
    equivalent
        ||
        
for r in range(m):
    for c in range(n):
        if r*c == 0:         #top-left edge
            dfs(r,c,0,visP) 
        if r==m-1 or c==n-1: #bottom-right edge
            dfs(r,c,0,visA)
            
        ||
    equivalent
        ||


for r in range(m):
    for c in range(n):
        # Perform edge checks
        if r == 0:  # Top edge 
            dfs(r, c, 0, visP)
        if r == m-1:  # Bottom edge
            dfs(r, c, 0, visA)
        if c == 0:  # Left edge
            dfs(r, c, 0, visP)
        if c == n-1:  # Right edge
            dfs(r, c, 0, visA)
'''


#Same Approach: DFS Using Array

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)        # m -rows
        n  = len(heights[0])       # n - cols
        
        seenP = [[False] * n for _ in range(m)]
        seenA = [[False] * n for _ in range(m)]
        
        def dfs(i: int, j: int, h: int, seen: list[list[bool]]) -> None:                                                                                   
            #(i,j) -current corrdinates , h-current cell height, seen - current array 
            if i<0 or i>=m or j<0 or j>=n:              #Out of bounds
                return
            
            if seen[i][j] or heights[i][j] < h:         #Question conditions not satisfied then return                              
                return             
            
            seen[i][j]=True                              #Mark current cell seen                               
            
            #Recursively perform DFS in all four directions.
            dfs(i+1,j,heights[i][j],seen)
            dfs(i-1,j,heights[i][j],seen)
            dfs(i,j-1,heights[i][j],seen)
            dfs(i,j+1,heights[i][j],seen)
            
        for r in range(m):
            for c in range(n):
                if r*c==0:             # top-left edge
                    dfs(r,c,0,seenP)
                if r ==m-1 or c ==n-1: # bottom-right edge
                    dfs(r,c,0,seenA)
            
        return [(i,j) for i in range(m) for j in range(n) if seenP[i][j] and seenA[i][j]]





