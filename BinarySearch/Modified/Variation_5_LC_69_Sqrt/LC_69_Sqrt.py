class Solution:
    def mySqrt(self,x):
        l ,r = 0 , x 
        while l<=r:
            m = floor((l+r)//2)
            if m*m > x:
                l = m +1
            elif m*m ==x:
                return m
            else:
                r = m - 1
       #at the end of the while loop left has reached right+1 i.e l = r +1
        return r #because in question we are asked to return the greatest integer n such that n**2<=x
        