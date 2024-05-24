#Solution 2: Writing our own reverse & transpose function
class Solution:
    def rotateAnti(self, matrix):

        def reverseList(arr):
            #Two Pointer approach to reverse a list
            n = len(arr)
            for i in range(n//2):
                arr[i],arr[n-1-i]=arr[n-1-i],arr[i]

        def transpose(grid):
            m , n = len(grid), len(grid[0])
            for r in range(m):
                for c in range(r): #cols will go upto r ,because if we can access the element along the bottom half of the diagonal then just by reversing c & r we can access the upper half of the diagonal too    
                    grid[r][c],grid[c][r] = grid[c][r],grid[r][c]
        

        #transpose i.e swap along the diagonal
        transpose(matrix)

        #mirror along the middle i.e swap the rows or reverse the 2D list/matrix/grid
        reverseList(matrix)

        return matrix


if __name__=="__main__":
    sol = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    expected_output =  [[3,6,9],[2,5,8],[1,4,7]]
    actual_output = sol.rotateAnti(matrix)
    print('actual_output',actual_output)
    print('Test1',expected_output==actual_output)




#Variation
# ALGORITHM TO ROTATE A 2D MATRIX/IMAGE 90 DEGREE CLOCKWISE
# To perform an anticlockwise – we can actually conduct there clockwise rotations. Alternatively, after matrix/image transpose, we can reverse the entire rows aka first row with the last row, the second row with the second-last row ..

class Solution:
    def rotateAntiClockwise(self, matrix):
        
        def transpose(grid):
            m , n = len(grid) ,len(grid[0])
            T = [[0]*m for _ in range(n)]
            for i in range(m):
                for j in range(n):
                    T[j][i] = grid[i][j]

            return T

        matrix[:] = transpose(matrix)

        R = len(matrix)
        for i in range(R//2):
            matrix[i], matrix[R -1-i] = matrix[R-1-i], matrix[i]

        return matrix

if __name__=="__main__":
    sol = Solution()
    matrix = [[1,2,3],[4,5,6]]
    expected_output =  [[3, 6], [2, 5], [1, 4]]
    actual_output = sol.rotateAntiClockwise(matrix)
    print('actual_output',actual_output)
    print('Test1',expected_output==actual_output)


# The time complexity is O(RC) and the space complexity is O(RC) although we can do this inplace if the R=C.




   
        