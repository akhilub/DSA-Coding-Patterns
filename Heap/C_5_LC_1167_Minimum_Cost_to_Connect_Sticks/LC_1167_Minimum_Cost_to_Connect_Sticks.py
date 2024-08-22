# Approach: Greedy + Priority Queue (Min Heap)

'''
We can use a greedy approach, each time choosing the shortest two sticks to connect, 
which ensures the minimum cost of connection.

Therefore, we can use a priority queue (min heap) to maintain the current stick lengths. 
Each time, we take out two sticks from the priority queue to connect, 
then put the connected stick back into the priority queue, 
until there is only one stick left in the priority queue.

The time complexity is O(n×logn), and the space complexity is O(n). Here, 

n is the length of the array sticks.
'''

# Example
# Assuming we are given four sticks with lengths a, b, c, and d respectively. The total costs would be (merging from left to right):

# connect a and b with cost a + b;
# connect a+b and c with cost a + b + c;
# connect a + b + c and d with cost a + b + c + d;

# Total costs: 3a + 3b + 2c + d. Thus, it is optimial to greedily pick the two smallest (a and b) every round in order to achieve the minimal total costs.

# By using the min heap in Python (the heapify module), we can simulate the process by popping out two smallest from the Priority Queue, accumulate the cost, and add the new stick (merged length) back to the priority queue.



class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        ans = 0
        while len(sticks)>1:
            s1  = heappop(sticks)
            s2  = heappop(sticks)
            ans+=s1+s2
            heapush(sticks,s1+s2)
        return ans