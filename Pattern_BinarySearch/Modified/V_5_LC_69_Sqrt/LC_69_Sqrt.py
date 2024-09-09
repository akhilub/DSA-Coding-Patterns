#Approach:Binary Search
#Time Complexity: O(logN) and the space complexity is O(1).
#Every iteration, we half the search space (by moving corresponding left or right pointer) until we either find the answer or left and right pointer meet somewhere in the middle.


#Binary Search Algorithm
# We define the left boundary of the binary search as l = 0 and the right boundary as r = x,
# then we search for the square root within the range [l, r].

# In each step of the search, we find the middle value mid = (l + r)//2 or (l+r+1)>>1 or (l+(r-l)/2)

# If mid*mid > x, it means the square root is within the range [l, mid - 1], 
# so we set r = mid - 1.
# Otherwise, it means the square root is within the range [mid, r],
# so we set l = mid + 1

# After the search ends, we return r.

class Solution:
    def mySqrt(self,x):
        #Binary Search f(i) = i**2
        l ,r = 0 , x 
        while l<=r:
            m = floor((l+r)/2) #stick to this
            if m*m == x:
                return mid
            elif m*m > x:
                r = m - 1
            else:
                l = m + 1
       #at the end of the while loop left has reached right+1 i.e l = r +1
        return r #because in question we are asked to return the greatest integer n such that n**2<=x


'''
floor((l+r)/2)
or
(l+r)//2
or
l +(r-l)//2
or
r+(l-r)//2
or
(l+r)>>1
'''