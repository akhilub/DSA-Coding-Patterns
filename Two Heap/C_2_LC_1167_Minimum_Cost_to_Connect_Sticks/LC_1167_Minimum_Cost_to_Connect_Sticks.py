# GREEDY STRATEGY BY PICKING TWO SMALLEST
# Assuming we are given four sticks with lengths a, b, c, and d respectively. The total costs would be (merging from left to right):

# connect a and b with cost a + b;
# connect a+b and c with cost a + b + c;
# connect a + b + c and d with cost a + b + c + d;

# Total costs: 3a + 3b + 2c + d. Thus, it is optimial to greedily pick the two smallest (a and b) every round in order to achieve the minimal total costs.

# By using the min heap in Python (the heapify module), we can simulate the process by popping out two smallest from the Priority Queue, accumulate the cost, and add the new stick (merged length) back to the priority queue.


import heapq as hq 

class Solution:
    def connectSticks(self,sticks:List[int])-> int:
        hq.heapify(sticks)
        ans = 0
        while len(sticks)>1:
            p , q = hq.heappop(sticks),hq.heappop(sticks)

            ans = ans + p + q
            hq.heappush(sticks, p+q )

        return ans

# The time complexity is O(NLogN) where N is the number of the sticks, and O(LogN) for the costs of pushing/popping element to/from the heap.
# Space complexity is O(N) for the heap/priority queue.