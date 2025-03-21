# Approach:DFS-Matrix

"""
We can start from the boundary of the matrix, taking each 'O' on the matrix boundary as a starting point,
and perform depth-first search. All 'O's found in the search are replaced with 'v'.

Then we traverse the matrix again, for each position:

If it is 'v', replace it with 'O';
Otherwise, if it is 'O', replace it with 'X'.

The time complexity is O(m×n), and the space complexity is O(m×n).
Here, m and n are the number of rows and columns in the matrix, respectively.
"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:  # Out of bounds
                return
            if board[i][j] != "O":  # Apply Question condition
                return

            board[i][j] = "v"  # S2- Mark the cell as visited

            # S-3 Explore in 4 directions
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for r in range(m):
            for c in range(n):
                # S1 - Enter the grid at the appropriate location as per the question conditons
                if (
                    r * c == 0 or r == m - 1 or c == n - 1
                ):  # Start from only the boundary here
                    dfs(r, c)

        # Traverse the board again
        for r in range(m):
            for c in range(n):
                board[r][c] = "O" if board[r][c] == "v" else "X"


"""
for r in range(m):
    for c in range(n):
        if r*c == 0 or r==m-1 or c ==n-1:             
            dfs(r,c)

            
        ||
    equivalent
        ||


for r in range(m):
    #left-right edge
    dfs(r,0)
    dfs(r,n-1)

for c in range(n):
    #top-bottom edge
    dfs(0,c)
    dfs(m-1,c)
"""


# Approach:BFS-Matrix
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()

        for r in range(m):
            for c in range(n):
                # select the border cells
                if r * c == 0 or r == m - 1 or c == n - 1:
                    if board[r][c] == "O":
                        q.append((r, c))

        # BFS to check the connectivity of border cells to those cells which are 'O'
        while q:
            i, j = q.popleft()
            board[i][j] = "v"  # temp assign new cell value
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    if board[ni][nj] == "O":
                        q.append((ni, nj))

        # Replace all 'O's with 'X' and 'v's back to 'O'
        for r in range(m):
            for c in range(n):
                board[r][c] = "O" if board[r][c] == "v" else "X"


# Write BFS using the above approach because here we have to mark the visited cell value twice
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m, n = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # BFS to check the connectivity of border cells to those cells which are 'O'
        def bfs(i, j):
            board[i][j] = "v"  # temp assign new cell value
            q = deque([(i, j)])
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        if board[nr][nc] == "O":
                            board[nr][nc] = "v"  # temp assign new cell value
                            q.append((nr, nc))

        # Step 1: Process all border cells
        for r in range(m):
            for c in range(n):
                if r in {0, m - 1} or c in {0, n - 1}:  # Check if it's a border cell
                    if board[r][c] == "O":
                        bfs(r, c)

        # Step 2: Replace all 'O's with 'X' and 'v's back to 'O'
        for r in range(m):
            for c in range(n):
                board[r][c] = "O" if board[r][c] == "v" else "X"


# When input modification is not allowed
# Approach:BFS
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not modify board in-place.
        """
        m, n = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        vis = set()
        ans = [["X"] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                # select the border cells
                if r * c == 0 or r == m - 1 or c == n - 1:
                    if board[r][c] == "O" and (r, c) not in vis:
                        # ans[r][c]="v"     #....(1)
                        q.append((r, c))
                        vis.add((r, c))

        # BFS to check the connectivity of border cells to those cells which are 'O'
        while q:
            i, j = q.popleft()
            ans[i][j] = "v"  # ....(2)
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    if board[ni][nj] == "O" and (ni, nj) not in vis:
                        # ans[ni][nj]="v"    #.....(1)
                        q.append((ni, nj))
                        vis.add((ni, nj))

        # Replace all 'O's with 'X' and 'v's back to 'O'
        for r in range(m):
            for c in range(n):
                ans[r][c] = "O" if ans[r][c] == "v" else "X"

        # board[::] =ans
        return ans


"""
Note:Either enable ...(1) or ...(2) not both simulataneously
"""
