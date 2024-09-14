#Approach:Binary Search
#Capacity = Work/Time 
#Problem function is monotonically decresing and we are looking for minimum
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        L , R = max(weights) , sum(weights)      #L -min_capacity , R-max_capacity ,(numbers , not indices)
        while L <R:
            mid = (L+R)//2                       #mid - curr_capacity
            if self.daysTakenToShip(weights,mid)<=days:
                R = mid
            else:
                L = mid+1
        return R
        
    def daysTakenToShip(self,weights,capacity):
        cW , dT = 0 ,1                          #cW - current weight ,dT - days Taken
        for w in weights:                       #w - weight
            cW+=w 
            if cW>capacity:
                cW = w
                dT+=1
        return dT
    
    





'''Same Above using the bisect_left , see how to apply bisect_left'''
from bisect import bisect_left

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def daysTakenToShip(capacity):
            cW, dT = 0, 1               # cW - current weight, dT - days Taken
            for w in weights:           # Iterate over each weight.
                cW += w 
                if cW > capacity:
                    cW = w
                    dT += 1
            return dT
        
        l, r = max(weights), sum(weights)
        
        return l + bisect_left(range(l, r + 1), True, key=lambda mid: self.daysTakenToShip(mid)<=days)

        
    






























