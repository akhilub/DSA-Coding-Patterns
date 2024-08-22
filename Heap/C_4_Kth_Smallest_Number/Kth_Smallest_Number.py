#Approach:Heap (Max-Heap)
#TC:O(nlog(k))
#SC:O(k)
from heapq import *

class Solution:
  def findKthSmallestNumber(self, nums, k):
      pq = []
      for num in nums:
          heappush(pq,-num)             #We are negating the number/ele onto the heap to simulate a max-heap
          
          if len(pq)>k:
              heappop(pq)
        return -pq[0]