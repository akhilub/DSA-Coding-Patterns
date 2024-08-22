#Logarithm Pow Function

"""
Terminology x is base and n is exponent

Because we have the following properties:

            value                                primary                       secondary         
        {   1                                    , n=0                 ,           x!=0
        {   0                                    , x = 0               ,           n!=0
        {   (1/x)^(-n)                           , n is -ve 
x^(n) = {   x * x^(n-1)                          , n is odd            ,           x!=0
        {   (x * x)^(n/2)  or (x^(n/2)))^2       , n is even
              
"""


'''
Our function translates to 
         {    1                                         ,        n = 0
         {    1 / f(x , -n)                             ,        n < 0 
f(x,n) = {    x * f(x , n-1)                            ,        n is odd
         {    f( x*x ,  n//2 ) or f(x,n//2)*f(x,n//2)   ,        n is even
 
''' 


#Recursive implementation of logarithmic algorithm

class Solution:
    def pow(self, x: float, n: int) -> float:
        if n==0:                       # n is 0 
            return 1
        if n<0:                        # n is -ve 
            return 1/self.pow(x,-n)
        if n&1:  #or n%2 ==1           # n is odd
            return x*self.pow(x,n-1)
        return self.pow(x*x,n//2)      #n is even



'''
return self.pow(x*x,n//2)           #n is even

equivalent

y = self.pow(x,n//2)               #n is even
return y*y
'''



# Iterative

class Solution(object):
    def pow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Default values
        if n ==0 : return 1
        if n < 0 :
            x , n = 1.0/x , -n
        
        #iteratively
        ans = 1
        while n>=1:
            if n & 1:   # n is odd 
                ans = ans*x
            x = x*x
            n = n//2    # or n>>=1
        return ans
             

#Time Complexity : O(log(n))
#Space Complexity : O(1)           



#Competative Programming/Pythonic Way

def pow(x, n):
   return x**n

