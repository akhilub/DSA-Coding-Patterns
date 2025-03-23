# Approach_1:BFS


# When input modification is not allowed
# TC:O(mxn)
# SC:O(mxn)


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        vis = set()

        for r in range(r):
            for c in range(c):
                if grid[r][c] == "*":
                    q.append((r, c))
                    vis.add((r, c))  # Mark cell as visited

        ans = 0
        while q:
            ans += 1

            for _ in range(len(q)):
                i, j = q.popleft()
                for di, dj in directions:
                    nr, nc = i + di, j + dj
                    if 0 <= nr < m and 0 < nc < n:
                        if grid[nr][nc] == "#":
                            return ans
                        if grid[nr][nc] != "X" and (nr, nc) not in vis:
                            q.append((nr, nc))
                            vis.add((nr, nc))  # Mark cell as visited

        return -1


# When input modification is allowed

"""
According to the problem, we need to start from `*`, find the nearest `#`, and return the shortest path length.

First, we traverse the entire two-dimensional array to find the position of `*`, which will be the starting point for BFS, and put it into the queue.

Then, we start BFS, traversing the elements in the queue. Each time we traverse an element,
we add the elements in the four directions (up, down, left, and right) of it into the queue, until we encounter #, and return the current layer number.

The time complexity is O(mxn), and the space complexity is O(1). Here, m and n are the number of rows and columns of the two-dimensional array, respectively.
"""


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(1, 0), (0, -1), (0, 1), (-1, 0)]
        q = deque()

        # Find the start position '*'
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "*":
                    grid[r][c] = "X"  # Mark cell as visited
                    q.append((r, c))

        ans = 0
        while q:
            ans += 1

            for _ in range(len(q)):
                i, j = q.popleft()
                for di, dj in directions:
                    nr, nc = i + di, j + dj
                    if 0 <= nr < m and 0 < nc < n:  # within the bounds
                        if grid[nr][nc] == "#":
                            return ans
                        if grid[nr][nc] == "O":  # meaning empty land
                            grid[nr][nc] = "X"  # First Mark cell as visited ,
                            q.append((nr, nc))  # then add to queue for processing

        return -1


"""
if grid[nr][nc] == "O":  # meaning empty land

                ||
                ||
                ||

if grid[nr][nc] != "X":   # meaning no obstacle
"""


# See the equivalency1
"""
i, j = next((i, j) for i in range(m) for j in range(n) if grid[i][j] == '*')
q = deque([(i, j)])

            ||
        equivalent
            ||

q = deque()
for r in range(m):
    for c in range(n):
        if grid[r][c] == "*":
            q.append((r, c))
            grid[r][c] = "X" 

"""

# See the equivalency2
"""
dirs = (-1, 0, 1, 0, -1)
for a, b in pairwise(dirs):
    x, y = i + a, j + b


    ||
equivalent
    ||

directions = [(1, 0), (0, -1), (0, 1), (-1, 0)]
for di, dj in directions:
    nr, nc = i + di, j + dj

"""


# Approach_1:Another way of writing BFS
from itertools import pairwise
from collections import deque
from typing import List


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        i, j = next((i, j) for i in range(m) for j in range(n) if grid[i][j] == "*")
        q = deque([(i, j)])
        dirs = (-1, 0, 1, 0, -1)
        ans = 0
        while q:
            ans += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for a, b in pairwise(dirs):
                    x, y = i + a, j + b
                    if 0 <= x < m and 0 <= y < n:
                        if grid[x][y] == "#":
                            return ans
                        if grid[x][y] == "O":
                            grid[x][y] = "X"
                            q.append((x, y))
        return -1
