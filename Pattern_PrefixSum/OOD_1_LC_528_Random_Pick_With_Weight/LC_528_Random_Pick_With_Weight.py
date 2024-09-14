#Approach1:Built-In
from itertools import *
from bisect import *
from random import *

class Solution:
    def __init__(self, w: List[int]):
        self.prefix = list(accumulate(w))
        
        

    def pickIndex(self) -> int:
        return bisect_left(self.prefix, random()*self.prefix[-1])


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()




#Approach:Binary Search + Prefix Sum
from random import *

class Solution:
    def __init__(self, w: List[int]):
        #print(w)
        self.s = [0]                     # intialized prefixSum list
        for c in w:
            self.s.append(self.s[-1]+c)  # Fill the list with prefix Sum's
        
        

    def pickIndex(self) -> int:
        x = randint(1,self.s[-1])        # x - random integer between 1 and last ele of prefixSum list
        l , r = 1 , len(self.s)-1
        while l<=r:
            mid = (l+r)//2
            if self.s[mid]>=x:
                r = mid-1
            else:
                l =mid+1
                
        return l-1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


