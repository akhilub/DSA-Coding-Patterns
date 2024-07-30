#Approach:
#1) We know to the algorithm to reverse a positive integer quickly
#2) We will keep a variable sign to make -ve integer to +ve ,pass the converted +ve integer to f(n) to retrieve its reverse and assign sign back based on original integer.
#3) Check for ans range to put in 

class Solution:
    def reverse(self,x):
        sign = -1 if x<0 else 1

        x*=sign

        res = self.pos_reverse(x)

        return sign*res if -2**31 <=res<= 2**31-1 else 0
    
    def pos_reverse(self,n):
        ans = 0
        while n!=0:
            r = n % 10
            ans = ans*10+r
            n = n//10
        return ans