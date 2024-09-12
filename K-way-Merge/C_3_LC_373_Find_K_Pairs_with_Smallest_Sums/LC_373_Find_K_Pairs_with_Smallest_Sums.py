#Approach:Min Heap
#TC:
#SC:

from heap import * # Importing heap functions for priority queue operations
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Priority Queue Initialization:
        pq = []                                                         # Initialize an empty priority queue (min-heap)
        for i in range(min(k,len(nums1))):
            pq.append((nums1[i]+nums2[0],i ,0))                         # Initialize the heap with the first k pairs (sum, index in nums1, index in nums2)
        heapify(pq)                                                     # Transform the list into a heap
        #print(pq)                                                      # pq is heapified
            
        
        
        ans =[]
        # Finding k Smallest Pairs:
        # Extract the k smallest pairs from the heap
        while pq and len(ans) <k:                                       # Continue until we have k pairs or the heap is empty  # added conditon `len(ans) < k` because we have to return only k pairs
            pos_sum , i , j = heappop(pq)                               # Pop the smallest element from the heap
            
            ans.append([nums1[i],nums2[j]])                             # Add the corresponding pair to the result
            
            # If there is another element in nums2 for the current nums1[i], push the new pair into the heap
            if j+1<len(nums2):
                
                heappush(pq,(nums1[i] + nums2[j + 1],i , j + 1))
                
        return ans                                                      # Return the list of k smallest pairs





'''
minHeap = []
for i in range(min(k, len(nums1))):
    heappush(minHeap, (nums1[i] + nums2[0], i, 0))
'''

#equivalent to 

'''
pq = []
for i in range(min(k,len(nums1)):
    pq.append((nums1[i]+nums2[0],i ,0))
heapify(pq)
'''











#MyApproach
#MLE

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        lst = [[v1, v2] for v1 in nums1 for v2 in nums2 ]
        
        lst2 = sorted(lst,key = lambda arr:arr[0]+arr[1])
        
        return lst2[:k]
        