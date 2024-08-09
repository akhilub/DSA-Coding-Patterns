#Approach: Rotate the image three times each time by 90 degree clockwise and check with target ,return true if rotated image matches the target

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat==target:
                return True

            self.rotateImage(mat)

        return False
    
    def rotateImage(self,mat):
            'In place modification of matrix'
            
            #swap along the middle
            def reverseList(arr):
                n = len(arr)
                for i in range(n//2):
                    arr[i],arr[n-1-i] = arr[n-1-i],arr[i]
            #swap symmetry i.e swap along the principal diagonal
            def transpose(grid):
                m = len(grid)
                for r in range(m):
                    for c in range(r):
                        grid[r][c],grid[c][r] = grid[c][r],grid[r][c]

            #Reverse the rows i.e     
            # Reverse the rows (flip upside down)
            reverseList(mat)
            # Transpose the matrix 
            transpose(mat)




#Competative Programming/Pythonic Way
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        for _ in range(4):
            if mat ==target:
                return True

            self.rotateImage(mat)
        
        def rotateImage(self,grid):
            #Copied the transformed 2D grid(first reverses ,then transposed) back into original mat
            #This updates mat in place with the newly rotated matrix. The slice assignment mat[:] ensures that the original list object mat is modified directly, which is necessary for the changes to persist outside the function scope.
            mat[:] = [list(row) for row in zip(*grid[::-1])]

        return False

        





