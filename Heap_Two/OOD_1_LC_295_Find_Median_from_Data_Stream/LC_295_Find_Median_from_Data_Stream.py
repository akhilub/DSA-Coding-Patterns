#Approach:Priority Queue(MinHeap & MaxHeap)

# Since the data in the data stream is not in order, we should first think of a way to make it in ordered. 
# If we use a vector to save the data stream, we must sort the array every time a new data comes in, which is not efficient.
# Use large and small heaps to solve the problem, where the large heap holds the larger numbers in the right half, and the small heap holds the smaller numbers in the left half.
# In this way, the entire array is divided into two sections in the middle. Since the heap is saved from large to small, we hope that the data in the large pile is from small to large, 
# so it is convenient to take the first one to calculate the median.


#Implementation
'''
We can use two heaps to maintain all the elements, a min heap `minQ` and a max heap `maxQ`, where the min heap 
`minQ` stores the larger half, and the max heap `maxQ` stores the smaller half.

When calling the addNum method, we first add the element to the max heap`maxQ` then pop the top element of `maxQ`and add it to the min heap `minQ`. 
If at this time the size difference between `minQ` and`maxQ`is greater than 1, 
we pop the top element of `minQ` and add it to`maxQ` 

The time complexity is O(logn).

When calling the findMedian method, 
If the size of `minQ` is equal to the size of `maxQ` it means the total number of elements is even, and we can return the average value of the top elements of 
`minQ` and`maxQ` otherwise, we return the top element of `minQ`. 
The time complexity is O(1).

The space complexity is O(n), where n is the number of elements.

'''



# Follow up
# Q-1: If all integer numbers from the stream are between 0 and 100, how would you optimize it?
# • We can maintain an integer array of length 100 to store the count of each number along with a total count. Then, we can iterate over the array to find the middle
# value to get our median. Time and space complexity would be 0(100) = 0(1) .


# Q-2: If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
# • In this case, we can keep a counter for lessThanHundred and greaterThanHundred. As we know the solution will be definitely in 0-100 we don't need to know those number which are >100 or <0, only count of them will be enough


from heapq import heappush, heappop
class MedianFinder:
    def __init__(self):
        self.min_pq=[]          # the larger half of the list, min heap
        self.max_pq=[]          # the smaller half of the list, max heap (invert min-heap)
        
        
    def addNum(self,num:int)->None:
        heappush(self.max_pq,-num)
        heappush(self.min_pq, -heappop(self.max_pq))
        
        if len(self.min_pq)-len(self.max_pq)>1:
            heappush(self.max_pq,-heappop(self.min_pq))        
        
    def findMedian(self)->float:
        if len(self.min_pq)==len(self.max_pq):  #even no of elements
            return (-self.max_pq[0]+self.min_pq[0]) / 2
        return self.min_pq[0]
        
        
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


'''
heappush(self.max_pq,-num)
heappush(self.min_pq, -heappop(self.max_pq)) 
                ||
                ||equivalent
                ||
heappush(self.min_pq,-heappushpop(self.max_pq,-num))
'''

