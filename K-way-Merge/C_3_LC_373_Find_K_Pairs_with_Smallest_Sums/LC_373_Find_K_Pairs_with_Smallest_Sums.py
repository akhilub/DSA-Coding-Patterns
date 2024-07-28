from heap import *
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq = []
        
        for i in range(min(k,len(nums1))):
            pq.append((nums1[i]+nums2[0],i ,0))
        heapify(pq)
        #print(pq) #pq is heapified
            
        ans =[]
        
        while pq and len(ans) <k: # added conditon `len(ans) < k` because we have to return only k pairs
            pos_sum , i , j = heappop(pq)
            
            ans.append([nums1[i],nums2[j]])
            
            if j+1<len(nums2):
                
                heappush(pq,(nums1[i] + nums2[j + 1],i , j + 1))
                
        return ans



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
        lst = [[ele1, ele2] for ele1 in nums1 for ele2 in nums2 ]
        
        lst2 = sorted(lst,key = lambda arr:arr[0]+arr[1])
        
        return lst2[:k]
        