#Approach: Heap(Max-heap)
#TC:O(nlog(n)) because building a heap take logn time , pushing n elements further takes nlogn , poping the largest element from heap takes logn
#SC:O(n)




from heap import *
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        pq = []                             # Initialize an empty list to use as a max-heap
        for i,num in enumerate(nums):       # Push the negative of each number along with its index into the heap.This effectively turns the heap into a max-heap
            heappush(pq,(-num,i))
            
        # Pop the largest element (i.e., the peak) from the heap    
        peak_num,peak_i = heappop(pq)
        return peak_i               # Return the index of the peak element
    

#Follow Up:You must write an algorithm that runs in O(log n) time.
#Approach:Binary Search(Monotonically decreasing)


'''
We define the left boundary of binary search as left=0 and the right boundary as right=n−1, 
where n is the length of the array. In each step of binary search, we find the middle element 

mid of the current interval, and compare the values of mid and its right neighbor mid+1:

If the value of mid is greater than the value of mid+1, there exists a peak element on the left side, 
and we update the right boundary right to mid.

Otherwise, there exists a peak element on the right side, and we update the left boundary 
left to mid+1.

Finally, when the left boundary left is equal to the right boundary right, we have found the peak element of the array.
The time complexity is O(logn), where n is the length of the array nums. Each step of binary search can reduce the search interval by half, so the time complexity is 
O(logn). The space complexity is O(1).
'''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l ,r = 0 , n-1
        while l <r:
            mid = (l+r)//2
            if nums[mid]>=nums[mid+1]:
                r = mid
            else:
                l = mid+1
