# Approach 1:Priority Queue (Min Heap)
'''
We can maintain a min heap `pq` of size `k` and then iterate through the array `nums` adding each element to the min heap. 
When the size of the min heap exceeds `k`, we pop the top element of the heap. This way, the final `k` elements in the min heap are the 
`k` largest elements in the array, and the top element of the heap is the kth largest element.

The time complexity is `O(nlogk)`, and the space complexity is `O(k)`. 
Here, `n` is the length of the array `nums`.

'''

# 1)Using nlargest
from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return nlargest(k, nums)[-1]
    
# 1)Using heap operations (min-Heap)
from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []                                             #1.Use a min-heap of size k to keep track of the k largest elements.
        for num in nums:
            heappush(pq,num)                                #2.Iterate through the array, adding elements to the heap.
            
            if len(pq)>k:                                   #3.If the heap size exceeds k, remove the smallest element from the heap.
                heappop(pq)
                
        return pq[0]                                        #4.The root of the heap will be the k-th largest element.


#Approach 3:Counting Sort

'''
We can use the idea of counting sort, counting the occurrence of each element in the array `nums`
and recording it in a hash table `cnt`. Then, we iterate over the elements `i` from largest to smallest, subtracting the occurrence count 
`cnt[i]` each time, until k is less than or equal to 0. At this point, the element `i` is the kth largest element in the array.

The time complexity is O(n+m), and the space complexity is O(n). Here, n is the length of the array `nums`, and `m` is the maximum value among the elements in `nums`.
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        for i in count(max(cnt),-1): #notice here it is `count` not `range`
            k-=cnt[i]
            if k<=0:
                return i
    
    
#Approach 2:Quick Select
#TC:O(n) average