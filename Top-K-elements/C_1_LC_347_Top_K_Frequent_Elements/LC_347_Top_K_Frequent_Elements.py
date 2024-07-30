# TOP K FREQUENT ELEMENTS VIA COUNTER’S MOST_COMMON
# The Counter returns a dictionary (hash map) that stores the key-value pairs (items) where keys are numbers/elements and values are the corresponding frequencies. We can returned the most common items by using the most_common method.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        return [key for key,val in c.most_common(k)]
    
# It does not provide a least common, but we can workaround by most_common (sorted in the descending order of the frequencies):

'''
c.most_common()[-1]
'''

# TOP K FREQUENT ELEMENTS VIA SORTING BY THE COUNTER’S ITEMS
# The most_common is essential sorting the items by the values (frequencies).


#My Approach
#Intial Solution    
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        a = sorted(c.items(), key= lambda p:p[1],reverse = True)
        return [i for i, j in a[:k]]


    

# TOP K FREQUENT ELEMENTS VIA HEAP
# The heapq in Python is a Min Heap (the heap.pop returns the smallest element). We can negate the numbers to make it a max heap. The algorithm pushes all the items in the form of -frequency, num tuple, then extracts k times to retrieve the Top K Frequent elements.
#Time Complexity : O(nlog(m))

#Write this in interviews
from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        a = []
        for num , freq in c.items():
            heappush(a,(-freq,num))
            
        ans = []
        for _ in range(k):
            _ , num = heappop(a)
            ans.append(num)
        return ans
    


# We can use the nlargest:
from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        a = []
        for num,freq in c.items():
            heappush(a,(freq,num))
        return [ j for i,j in heapq.nlargest(k,a,key = itemgetter(0))]
    
# or nsmallest
from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        a = []
        for num , freq in c.items():
            heappush(a, (-freq,num))      #Notice the negative sign
            
        return [j for i,j in heapq.nsmallest(k,a,key = itemgetter(0))]
    
    