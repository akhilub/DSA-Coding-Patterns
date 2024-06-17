#Approach:Heap

# Since the data in the data stream is not in order, we should first think of a way to make it in ordered. If we use a vector to save the data stream, we must sort the array every time a new data comes in, which is not efficient.
# Use large and small heaps to solve the problem, where the large heap holds the larger numbers in the right half, and the small heap holds the smaller numbers in the left half.
# In this way, the entire array is divided into two sections in the middle. Since the heap is saved from large to small, we hope that the data in the large pile is from small to large, so it is convenient to take the first one to calculate the median.


# Follow up
# Q-1: If all integer numbers from the stream are between 0 and 100, how would you optimize it?
# • We can maintain an integer array of length 100 to store the count of each number along with a total count. Then, we can iterate over the array to find the middle
# value to get our median. Time and space complexity would be 0(100) = 0(1) .


# Q-2: If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
# • In this case, we can keep a counter for lessThanHundred and greaterThanHundred. As we know the solution will be definitely in 0-100 we don't need to know those number which are >100 or <0, only count of them will be enough


from heap import heapush, heappop

class MedianFinder:

    def __init__(self):
        # the smaller half of the list, max heap (invert min-heap)
        self.smallerHalf = []
        # the larger half of the list, min heap
        self.largerHalf = []

    def addNum(self, num: int) -> None:
        # trick for smaller half, use -1*val
		# heapq in python does NOT have comparator like in Java
        heapush(self.smallerHalf,-num)
        heappush(self.largerHalf,-heappop(self.smallerHalf))   # note: not self.smallerHalf.pop()

        if len(self.smallerHalf) < len(self.largerHalf):
            heappush(self.smallerHalf, -heappop(self.largerHalf))

    
    def findMedian(self)-> float:
        if len(self.smallerHalf) == len(self.largerHalf):
            return (-self.smallerHalf[0] + self.largerHalf[0]) / 2.0
		else:
			return float(-self.smallerHalf[0])





#Write this in interviews
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.h1 = []
        self.h2 = []

    def addNum(self, num: int) -> None:
        heappush(self.h1, num)
        heappush(self.h2, -heappop(self.h1))
        if len(self.h2) - len(self.h1) > 1:
            heappush(self.h1, -heappop(self.h2))

    def findMedian(self) -> float:
        if len(self.h2) > len(self.h1):
            return -self.h2[0]
        return (self.h1[0] - self.h2[0]) / 2
