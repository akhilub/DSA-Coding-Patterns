#Approach:Trie
from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # When a word ends at this node

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build the Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word  # Mark the end of a word
        

        R, C = len(board), len(board[0])
        ans = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        def dfs(i, j, parent):
            # Out of bounds check
            if i < 0 or i >= R or j < 0 or j >= C:
                return
            
            char = board[i][j]
            # Visited check
            if char == '#':
                return

            #if the character is not in the current Trie node
            if char not in parent.children:
                return
            
            node = parent.children[char]
            
            # Check if we found a word
            if node.word:
                ans.append(node.word)
                node.word = None  # Avoid duplicate entries

            # Mark the current cell as visited
            board[i][j] = '#'

            # Explore neighbors
            for di, dj in directions:
                dfs(i + di, j + dj, node)

            # Restore the current cell
            board[i][j] = char

            # Optimization: remove the leaf node to save memory and time
            if not node.children:
                parent.children.pop(char)

        for r in range(R):
            for c in range(C):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return ans






















#TLE
#Approach:Backtacking 
#Extension of LC 79 Word Search 

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R , C = len(board) , len(board[0])
        visited = set()
        def dfs(i,j,idx):
            #base cases
            
            if idx == len(word):
                return True
            
            if i<0 or i>=R or j<0 or j>=C:
                return False
            
            if board[i][j]!=word[idx]:
                return False
            
            if (i,j) in visited:
                return False
            
            #add
            visited.add((i,j))
            
            #explore
            res = dfs(i+1,j,idx+1) or dfs(i-1,j,idx+1) or dfs(i,j+1,idx+1) or dfs(i,j-1,idx+1)
            #remove        
            visited.remove((i,j))
            
            return res
            
        
        ans = []
        for r in range(R):
            for c in range(C):
                for word in words:
                    if word not in ans and board[r][c] == word[0]:
                        if dfs(r,c,0):
                            ans.append(word)
        return ans













































