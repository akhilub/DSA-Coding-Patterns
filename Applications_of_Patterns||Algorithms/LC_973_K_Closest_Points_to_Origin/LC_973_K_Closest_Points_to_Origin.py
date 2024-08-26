#Approach1:Custom Sorting
'''
We sort all points by their distance from the origin in ascending order, and then take the first k points.

The time complexity is O(nlogn), and the space complexity is O(logn). Here, n is the length of the array points.
'''

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        sort_arr = sorted(points,key = lambda p :sqrt(p[0]**2+p[1]**2))
        return sort_arr[:k]

'''
sort_arr = sorted(point,key =lambda p:sqrt(p[0]**2+p[1]**2))
                        ||
sort_arr = sorted(point,key =lambda p:p[0]**2+p[1]**2)
                        ||                        
sort_arr = sorted(point,key =lambda p:hypot(p[0],p[1]))

'''



#Approach2:Priority Queue(Max-Heap)
'''
We can use a priority queue (max heap) to maintain the k closest points to the origin.

The time complexity is O(n×logk), and the space complexity is O(k). Here, n is the length of the array points.
'''

from math import *
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_pq = []
        for i , (x,y) in enumerate(points):
            dist = hypot(x,y)
            heappush(max_pq,(-dist,i))
            
            if len(max_pq)>k:
                heappop(max_pq)
                
        return [points[i] for _, i in max_pq]
    
    
#Approach3:Binary Search
#Not required