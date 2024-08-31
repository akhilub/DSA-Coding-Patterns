#Approach:MinHeap or Priority Queue
#TC: O(nlog(k)) where n is the number of elements in a list and k are the number of lists
from heapq import *
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ans = self.mergeKSortedArrays(matrix)
        return ans[k-1]

    def mergeKSortedArrays(self,lists:List[List[int]]):
        pq = []
        for i ,arr in enumerate(lists):
            pq.append((arr[0],i,0))         #`0`: the index of the current element in the list arr , i - current array index, arr[0]- current array Oth index element
        heapify(pq)

        res = []

        while pq:
            s_val ,li, ei = heappop(pq)     #s_val - smallest value, li- list index, ei-current element index 
            res.append(s_val)

            n_ei = ei+1                     #n_ei - next/neighbor element index
            if n_ei <len(lists[li]):
                next_val = lists[li][n_ei]
                heappush(pq,(next_val,li, n_ei))

        return res
        

'''
pq = [(arr[0],i,0) for i,arr in enumerate(lists) if arr]

better than

pq = []
for i ,arr in enumerate(lists):
    pq.append((arr[0],i,0)) 
'''

'''
pq = []
for i , arr in enumerate(lists):
    heappush(pq,(arr[0],i,0))
    
equivalent to 

pq = []
for i ,arr in enumerate(lists):
    pq.append((arr[0],i,0))
heapify(pq)
'''



#Competative Programming 
#Approach:MinHeap or Priority Queue(Compressed Above approach only)
class Solution:
    
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ans = self.mergeKSortedArrays(matrix)
        return ans[k-1]
        
    def mergeKSortedArrays(self,lists:List[List[int]]):
        return list(heapq.merge(*lists))






#Approach:Divide & Conquer
#TC:O(nlog(k))
class Solution:
    
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ans = self.mergeKSortedArray(matrix)
        return ans[k-1]
        
    def mergeKSortedArray(self,lists:List[List[int]]):
        K = len(lists) #there are K list inside array lists
        if K==1:
            return lists[0]
        mid = K//2
        left = self.mergeKSortedArray(lists[:mid])
        right = self.mergeKSortedArray(lists[mid:])
        return self.mergeTwoSortedArray(left,right)

    def mergeTwoSortedArray(self,a,b):
        i , j ,la,lb =0,0,len(a),len(b)
        res = []
        while i<la and j<lb:
            if a[i]<b[j]:
                res.append(a[i])
                i+=1
            else:
                res.append(b[j])
                j+=1
        if i<la:
            res+=a[i:]
        if j<lb:
            res+=b[j:]
        
        return res
    
    





#Follow up:Best Approach ->Binary Search






