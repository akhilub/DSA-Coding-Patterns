# Multi-source BFS
# I repeat do not try with DFS (TLE) stick to BFS

'''
We create a matrix `ans` of the same size as `mat` and initialize all elements to -1.

Then, we traverse `mat`, adding the coordinates (i,j) of all 0 elements to the queue q, 
and setting ans[i][j] to 0.

Next, we use Breadth-First Search (BFS), removing an element (i,j) from the queue and traversing its four directions. 
If the element in that direction (x,y) satisfies 0≤x<m, 0≤y<n and ans[x][y]= -1, 
then we set ans[x][y] to ans[i][j]+1 and add (x,y) to the queue q.

Finally, we return ans.

The time complexity is O(m x n), and the space complexity is O(m x n). Here, m and n are the number of rows and columns in the matrix `mat`, respectively.
'''



#Write this in interviews
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m , n = len(mat) , len(mat[0])
        # Initialize the result matrix ans, where the distance of all zeros is 0, and thus the distance of all ones is -1.
        ans = [[-1]*n for _ in range(m)]
        
        # Initialize a queue q to store the positions to be checked by BFS, and enqueue all positions of zeros.
        q = deque()
        for r in range(m):
            for c in range(n):
                if mat[r][c]==0:
                    ans[r][c]=0
                    q.append((r,c))
        
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        # Continually dequeue elements p(i, j) from queue q, inspecting the four neighboring points.
        # For each neighbor (x, y), if ans[x][y] = -1, then update ans[x][y] = ans[i][j] + 1.
        while q:
            r,c = q.popleft()
            for dr , dc in directions:
                nr = r + dr
                nc = c + dc
                if 0<=nr<m and 0<=nc=n:
                    if ans[nr][nc]==-1:
                        ans[nr][nc]=ans[r][c] + 1       #Only This `1` will change to appropriate distance if tommorrow the matrix is of 1&2 
                        q.append((nr,nc))               # Also, enqueue the position (x, y).
                        
        return ans 




#My Approach
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n= len(mat[0])
        q= deque()
        visited = set()
        dist = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    
                    q.append((i,j,0)) # (curr row, curr col, intial distance)
                    visited.add((i,j))

        directions =((0,1),(0,-1),(1,0),(-1,0))
        while q:
            i,j,d = q.popleft()
            dist[i][j]=d

            for di,dj in directions:
                ni = i+di
                nj = j+dj

                if 0<=ni<m and 0<=nj<n and (ni,nj) not in visited: #new cell within bounds and not visited
                    q.append((ni,nj,d+1))                          #add appropriate distance in d 
                    visited.add((ni,nj))

        return dist












