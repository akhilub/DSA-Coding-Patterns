#Approach :Min-Heap

'''
We use a min-heap to efficiently keep track of the 'K' largest numbers. 
The idea is to maintain a heap of size k:

1.Traverse the array and add elements to the heap.
2.If the heap size exceeds k, remove the smallest element (which is the root of the min-heap). This ensures that only the k largest elements remain in the heap.
3.Finally, the heap will contain the k largest elements.
'''

from heapq import *
class Solution:
    def findKLargestNumbers(self,nums,k):
        pq = []
        for num in nums:
            heappush(pq,num)
            
            if len(pq)>k:
                heappop(pq)
                
        return pq
    

# Explanation:
# Heap of size k: The heap is kept at size k. This way, the smallest element in the heap (root of the min-heap) is always the smallest among the k largest elements found so far.
# Efficiency: This approach runs in O(N log k) time, which is efficient for large input sizes.
