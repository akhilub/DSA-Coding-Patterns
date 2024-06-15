class Solution:
    def transpose(self,matrix):
        m , n = len(matrix),len(matrix[0])
        T = [[0]*m for _ in range(n)] # Transpose of matrix of size mxn will have n rows and m cols
        for r in range(m):
            for c in range(n):
                T[c][r] = matrix[r][c]

        return T



