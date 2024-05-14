#Backtracking 

#TC: O(M*N*DFS)  O(DFS) = 4*n    where n is the no of characters in word
#SC :O(M*N)
class Solution:
    def exist(exist,board,word):
        R , C =len(board),len(borard[0])
        visited = set () # To keep track of the visited cell so that do not visited it again

        def dfs(i,j,idx):
            #Base Cases
            if idx = len(word): #reached to the end of the word
                return True
            
            if i<0 or i>=R or j<0 or j>=C: #out of bounds
                return False
            
            if board[i][j]!=word[idx]: #letter from the word is not in board
                return False

            if (i,j) in visited: #visiting the same cell twice
                return False 


            visited.add((i,j))
            #Recursive Cases
            res = dfs(i+1,j,idx+1) or 
                  dfs(i,j+1,idx+1) or
                  dfs(i-1,j,idx+1) or
                  dfs(i,j-1,idx+1) or

            visited.remove((i,j))
            return res

        for row in range(R):
            for col in range(C):
                if board[r][c]==word[0]:
                    if dfs(r,c,0):
                        return True
        return False























#Backtracking(Recursive) BFS
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R , C = len(board), len(board[0])
        visited = set()
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        #bfs will return True if word exist in grid/board
        def bfs(i, j, k):
            q = deque([(i, j, k)])
            visited.add((i, j))
            while q:
                r, c, idx = q.popleft()
                #
                idx += 1              # Incrementing the word index
                if idx == len(word):  # Check if we've reached the end of the word
                    return True
                
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < R and 0 <= nc < C: 
                        if board[nr][nc] == word[idx] and (nr, nc) not in visited:
                            if bfs(nr, nc, idx):  # Recursively check the next character
                                return True
            visited.remove((r, c))                # Unmark the cell when backtracking from a failed path
            return False
                            
            
        for row in range(R):
            for col in range(C):
                if board[row][col] == word[0]:
                    if bfs(row,col,0):  #start the bfs when we find first matching letter
                        return True
        return False