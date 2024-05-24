#Approach 1:Transpose + Reflect
#We can first transpose the matrix, and then reverse each row – this will be virtually rotating a matrix 90 degree in two passes.


#Solution 1:Using in-built Python function
import numpy as np
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #mirror along the middle i.e swap the rows or reverse the 2D list/matrix/grid
        matrix.reverse()

        #transpose the matrix i.e swap the elementd along the diagonal
        matrix[:] = np.transpose(matrix)



#Solution 2: Writing our own reverse & transpose function
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        def reverseList(arr:List[int]):
            #Two Pointer approach to reverse a list
            n = len(arr)
            for i in range(n//2):
                arr[i],arr[n-1-i]=arr[n-1-i],arr[i]

        def transpose(grid: List[List[int]]):
            m , n = len(grid), len(grid[0])
            for r in range(m):
                for c in range(r): #cols will go upto r ,because if we can access the element along the bottom half of the diagonal then just by reversing c & r we can access the upper half of the diagonal too    
                    grid[r][c],grid[c][r] = grid[c][r],grid[r][c]
        

        #mirror along the middle i.e swap the rows or reverse the 2D list/matrix/grid
        reverseList(matrix)

        #transpose i.e swap along the diagonal
        transpose(matrix)



#Competative Programming/Pythonic Way

def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    matrix[:] = list(zip(*matrix[::-1]))


            



