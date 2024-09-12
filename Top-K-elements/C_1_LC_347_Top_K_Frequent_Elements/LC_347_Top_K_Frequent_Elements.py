# TOP K FREQUENT ELEMENTS VIA HEAP (Max-Heap)

# The heapq in Python is a Min Heap (the heap.pop returns the smallest element). 
# We can negate the numbers to make it a max heap. The algorithm pushes all the items in the form of (-frequency, num) tuple, 
# then extracts k times to retrieve the Top K Frequent elements.

# Time Complexity : O(nlog(m)) where `n` is the no of elements in `nums` and `m` is the no of elements in hashTable `c` (unique elements in nums)
# space complexity of O(m).


'''Write this in interviews(Stick to this only)'''

from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        pq = []                      #we will turn `pq` into max-heap
        for num , freq in cnt.items():
            heappush(pq,(-freq,num))
            
        ans = []
        for _ in range(k):
            _ , num = heappop(pq)
            ans.append(num) # ans+=[num]
        return ans











































#My Approach
#Intial Solution :Two HashTables
#TC:O(nlog(k))
#SC:O(k)

# TOP K FREQUENT ELEMENTS VIA SORTING BY THE COUNTER’S ITEMS

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each element in the list
        freqs = Counter(nums)

        # Sort the elements by frequency in decreasing order
        sorted_freqs = sorted(freqs.items(), key=lambda x: x[1], reverse=True)
        
        # Take the top k elements
        top_k = [num for num, freq in sorted_freqs[:k]]

        return top_k


'''
sorted_freqs = sorted(freqs.items(), key=lambda x: x[1], reverse=True)

equivalent

sorted_freqs = sorted(freqs.items(), key=lambda x: -x[1])

'''








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
# The most_common is essential sorting the items by the values (frequencies).





# We can use the nlargest:
from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        a = []
        for num,freq in c.items():
            heappush(a,(freq,num))
        return [j for i,j in heapq.nlargest(k,a,key = itemgetter(0))]
    
    

# or nsmallest
from heapq import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        a = []
        for num , freq in c.items():
            heappush(a, (-freq,num))      #Notice the negative sign
            
        return [j for i,j in heapq.nsmallest(k,a,key = itemgetter(0))]
    
    
    
    
    
    
    
    
    
    
    



















'''
>>> from heapq import heappush
>>> h = []
>>> heappush(h, (3,1))
>>> heappush(h, (1,1))
>>> heappush(h, (2,1))
>>> h
[(1, 1), (3, 1), (2, 1)]

>>> from heapq import heappop
>>> heappop(h)
(1, 1)
>>> heappop(h)
(2, 1)
>>> heappop(h)
(3, 1)
'''



#Approach: Hash Table + Priority Queue (Min Heap)

'''
We can use a hash table `cnt` to count the occurrence of each element, and then use a min heap (priority queue) to store the top 
k frequent elements.

First, we traverse the array once to count the occurrence of each element. Then, we iterate through the hash table, 
storing each element and its count into the min heap. 

If the size of the min heap exceeds `k`, we pop the top element of the heap to ensure the heap size is always `k`.

Finally, we pop the elements from the min heap one by one and place them into the result array.

The time complexity is O(nlogk), and the space complexity is O(k). Here, n is the length of the array.

'''


from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)   # find the frequency of each number
        pq = []               # min-heap
        
        '''
        go through all numbers of the numFrequencyMap `cnt` and push them in the minHeap, 
        which will have top k frequent numbers. If the heap size is more than k, we remove the 
        smallest(top) number
        '''
        for num , freq in cnt.items():
            heappush(pq,(freq,num))         # freq first, default sort by 1st element
            
            
            if len(pq)>k:
                heappop(pq)
        
        
        # create a list of top k numbers  
        ans = []
        while pq:
            ans.append(heappop(pq)[1])      
        return ans