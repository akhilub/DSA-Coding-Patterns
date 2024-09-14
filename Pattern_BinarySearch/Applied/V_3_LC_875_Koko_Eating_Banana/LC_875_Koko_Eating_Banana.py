#Approach:Binary Search

'''
We notice that if Koko can eat all the bananas at a speed of `k` within `h` hours, then she can also eat all the bananas at a speed of 
`k1 > k` within `h` hours. This shows monotonicity, so we can use binary search to find the smallest `k` that satisfies the condition.

We define the left boundary of the binary search as `L=1` and the right boundary as `R=max(piles)`. 
For each binary search, we take the middle value mid= (L+R)//2, and then calculate the time `t` required to eat bananas at a speed of `mid`. 

If t≤h, it means that the speed of `mid` can meet the condition, and we update the right boundary `R` to `mid`; otherwise, we update the left boundary 

`L` to `mid+1`. Finally, when L==R, we find the smallest `k` that satisfies the condition.

The time complexity is O(n×logM), where n and M are the length and maximum value of the array piles respectively. 
The space complexity is O(1).

'''

#Note:We are applying Binary search on speed array K = [1......max(piles)] i.e K= [1,2,3,4,5,6,7,8,9,10,11] when piles = [3,6,7,11]

from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L , R = 1 , max(piles)   #L & R are the min & max speed (numbers , not indices) to finish/eat array piles
        ans = R                  # We are trying to minimize ans (rate of eating)
        while L<R:
            
            mid = (L+R)//2       # mid, average speed of koko eating
            
            t = sum(ceil(x/mid) for x in piles)     #total time to eat each pile at speed mid at loose bound
            
            if t<=h:                #when the total time `t` approaches `h` we are sure we found a minimum speed `mid` and store it. 
                ans = min(ans,mid)
                R = mid
            else:
                L = mid+1
                
        return ans # L


    
#Speed = Banana/Time
#F(Speed) is monotonically decresing so update R towards mid when LESS_THAN_CONDITION


'''

t = sum(math.ceil(x/mid) for x in piles)
            ||
         equivalent
            ||
t = sum((x + mid - 1) // mid  for x in piles)
'''



#Another Way

