#Approach: Binary Search
#Given defination : t = (r)*(n)^2                 # t - time , r- rank of mechanic , n-#cars

#Problem function f(time) is monotonically increasing and we are looking for minimum time , 

# so update L towards mid when approaching towards cars count `cars` with time `mid`


# on x-axis we have time
# on y-axis we have N = f(time) = sqrt(t/r)      # N-total no of cars repaired in `time` minutes


#Algorithm
'''
We notice that the longer the repair time, the more cars are repaired. Therefore, we can use the repair time as the target of binary search, and binary search for the minimum repair time.

We define the left and right boundaries of the binary search as 

left= min(ranks)*1**2, right= max(ranks)*cars**2  

Next, we binary search for the repair time `mid`, and the number of cars each mechanic can repair is 
⌊√(mid/r)⌋, where ⌊x⌋ represents rounding down. 

If the number of cars repaired is less than to cars, it means that the repair time mid is feasible ,

we reduce the left boundary to `mid +1`, otherwise we reduce the right boundary to `mid`.

Finally, we return the left boundary.

The time complexity is O(n x logM), and the space complexity is O(1).
Here, n is the number of mechanics, and M is the upper bound of the binary search.

'''





'''
On macbook
√  - Option + V
'''


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def f(time):
            N = sum(isqrt(time//r)  for r in ranks)      #N- #cars repaired in different `mid` minutes
            return N
        
        L, R = min(ranks)*1**2, max(ranks)*cars**2       #L - min & R - max time  
        while L<R:
            mid = (L+R)//2
                                            
            if f(mid)<cars:                                 
                L = mid+1
            else:
                R = mid
                
        return L
    

'''

N = sum(isqrt(mid//r)  for r in ranks)
            ||
            OR
            ||
N = sum(int(sqrt(mid // r)) for r in ranks)
            ||
            OR
            ||
N = sum(floor(sqrt(mid/r)) for r in ranks)


if N<cars:


'''


#If you do not understand L, R bounds just take min & max contraints(bounds) given in problem description
# (10^6)*(10^5)**2 = 10**16
#L , R = 0 ,  10**16