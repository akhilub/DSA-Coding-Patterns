class Solution:
    def fib(self,n):
        prev , curr = 0, 1
        for _ in range(n):
            prev , curr = curr , prev + curr                
        return prev


#               1           1           2                  3                   5               8     
#              prev        curr
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