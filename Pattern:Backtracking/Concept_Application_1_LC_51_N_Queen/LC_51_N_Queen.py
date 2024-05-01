#Approach: Backtracking


#Chessboard of size NxN, MainDaigonal = 2N-1 , Anti-Diagonal = 2N-1

#We define three array col , mdiag , adiag to represent whether there is a queen in the column, main diagonal, anti diagonal respectively.

#If there is queen in the (i,j)position then col[j],mdiag[i+j] & adiag[n-1-i+j] are all True.In addition we will use an empty array board to record the current state of the chessboard

#Next Let define a function dfs(i) which represent placing queens starting from ith row. 

#In dfs if i == n ,it means that we have completed the placement of all queens.We put the current board array into the answer and end the recursion

#Otherwise we enumerate each column j of the current row .

#if there is no queen at the position(i,j) i.e col[j],mdiag[i+j] & adiag[n-1-i+j] are all False,

#then we can place a queen i.e 
#1) set col[j],mdiag[i+j] & adiag[n-i+j] to True
#2) change board[i][j] = Q and remaining all position at the ith row to '.' .
#3) Then we continue to search the next row i.e call dfs(i+1)
#4) After the recursion ends we need to update the col[j],mdiag[i+j] & adiag[n-i+j] back to False
#5) And during our search if we find col[j] or mdiag[i+j] or adiag[n-1-i+j] False , we skip that loop

#In the main function , we call dfs(0,[]) to start the array and return the answer array



class Solution:
    def solveNQueen(self,n):
        col = [False]*n
        mdiag = [False]*(2*n - 1)
        adiag = [False]*(2*n - 1)
        ans = []
        def dfs(i,board):
            if i == n:
                ans.append(board)
                return
            

            for j in range(n):
                if col[j] or mdiag[i+j] or adiag[n-1-i+j]:
                    continue
                col[j] = mdiag[i+j] = adiag[n-1-i+j] = True
                dfs(i+1, board + ['.' * j + 'Q' + '.'*(n-1-j)])
                col[j] = mdiag[i+j] = adiag[n-1-i+j] = False

        dfs(0,[])
        return ans




