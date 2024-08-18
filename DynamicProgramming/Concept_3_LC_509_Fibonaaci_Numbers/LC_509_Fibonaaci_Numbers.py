#Appraoch1) TopDown DP : Recursion +Memoization

class Solution:
    def fib(self, n: int) -> int:
        def f(i,nb={}):
            if i==0:
                return 0
            if i==1:
                return 1
            if i in nb:
                return nb[i]
            nb[i] = f(i-1)+f(i-2)
            return nb[i]
        return f(n)

#Appraoch2) Bottom Up DP : Tabulation

class Solution:
    def fib(self, n: int) -> int:
        dp = [0,1] +[0]*(n-1)                               
        
        for i in range(2,n+1):
            dp[i] = dp[i-1]+dp[i-2]
        
        return dp[n]
    
    
#Q)#How [0]*(n-1)? because total no of elements in the list are  `n+1`, out of `n+1` we have already defined twp `[0,1]` so the remaining are (n+1-2) = n-1 

#Approach3) Bottom Up: No Memory DP

#We don't need to store all the Fibonacci numbers up to 'n', as we only need two previous numbers to calculate the next Fibonacci number.

class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        
        f0,f1 = 0,1   #initial states to compute the next states
        for i in range(2,n+1):
            fi = f1+f0
            f0,f1 = f1,fi
        return fi




#Greedy 
class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a














#Analysis of Greedy

class Solution:
    def fib(self,n):
        prev , curr = 0, 1
        for _ in range(n):
            prev , curr = curr , prev + curr                
        return prev


#               1           1           2                  3                   5               8     
#  i = 0       prev        curr
#  i = 1                   prev = 1    curr = 1 + 1
#  i = 2                               prev = 2       curr = 1 + 2
#  i = 3                                                 prev = 3         curr = 2 + 3





#Do not do this , here we are using `new prev` to compute the `new curr` but we need `previous prev` & `previous curr` to compute the `new curr`
class Solution:
    def fib(self,n):
        prev , curr = 0, 1
        for _ in range(n):
            prev = curr
            curr = prev + curr                
        return prev