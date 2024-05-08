#Recursion 
class Solution:
    def solution(self,n):
        #terminate recursion
        if n==1:
            return 1
        return self.solution(n-1) + 4*n - 4


#DP
#Dynamic programming is a method for solving complex problems by breaking them down into simpler subproblems. 
#It involves solving each subproblem only once and storing the solution to avoid redundant calculations. 
#Dynamic programming is typically used when a problem can be divided into overlapping subproblems that can be solved independently. 
#This approach can lead to more efficient solutions compared to naive recursive approaches by avoiding recomputation of the same subproblems.

class Solution:
    def solution(self,n):
        def f(i,nb={}):
            #terminate/base cases
            if i ==1:
                return 1
            #dp subproblem take answers from here
            if i in nb:
                return nb[i]
            nb[i] = f(i-1) + 4*i - 4
            return nb[i]

        return f(n)

#Using Python Library

from functools import cache
class Solution:
    def solution(self,n):
        @cache
        def f(n):
            if n==1:
                return 1
            return f(n-1) + 4*n -4 
        return f(n)


if __name__== "__main__":
    sol = Solution()
    n = 1
    result = sol.solution(n)
    print('Test Case1',result)

    sol = Solution()
    n = 2
    result = sol.solution(n)
    print('Test Case2',result)

    sol = Solution()
    n = 3
    result = sol.solution(n)
    print('Test Case3',result)

    sol = Solution()
    n = 4
    result = sol.solution(n)
    print('Test Case4',result)

    sol = Solution()
    n = 5
    result = sol.solution(n)
    print('Test Case4',result)


