#Approach: K-way-merge or Min-Heap or Prirority Queue
# TC:O(n(log(k)))
# Write this in interviews

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []

        # Initialize the heap with the head of each linked list
        for i, node in enumerate(lists):
            if node:  # Check if the list is not empty
                pq.append((node.val, i, node))
        heapify(pq)

        dummy = ListNode()  # Dummy node to simplify the merging process
        curr = dummy

        while pq:
            # Extract the smallest element from the heap
            s_val, li, node = heappop(pq)
            curr.next = ListNode(s_val)
            curr = curr.next

            # Move to the next element in the same list and add it to the heap
            if node.next:
                heappush(pq, (node.next.val, li, node.next))

        return dummy.next


























# Approach2: Priority Queue (Min Heap)
# We can create a min heap pq to maintain the head nodes of all linked lists. 
# Each time, we take out the node with the smallest value from the min heap, add it to the end of the result linked list, 
# and then add the next node of this node to the heap. 
# Repeat the above steps until the heap is empty.
# The time complexity is O(nlog k), and the space complexity is O(k). Here, n is the total number of all linked list nodes, and k is the number of linked lists given in the problem.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import List, Optional
from heapq import heapify,heappush,heappop
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # Dynamically add a less-than method to ListNode to compare nodes by their val attribute
        setattr(ListNode, "__lt__", lambda a, b: a.val < b.val)

        # Filter out None values from the lists and create a priority queue (min-heap)
        pq = [head for head in lists if head]

        heapify(pq) # Transform the list into a heap
        #print(pq)

        # Create a dummy node to simplify the merge process
        dummy = cur = ListNode(0)

        # Process the heap until it's empty
        while pq:
             # Pop the smallest node from the heap
            node = heappop(pq)
            # If the popped node has a next node, push it into the heap
            if node.next:
                heappush(pq, node.next)
            # Link the current node to the merged list
            cur.next = node
            cur = cur.next
        # Return the merged list, starting from the node after the dummy
        return dummy.next

if __name__ == '__main__':

    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    l3 = ListNode(2)
    l3.next = ListNode(6)

    print(Solution().mergeKLists([l1, l2, l3]))

    print(Solution().mergeKLists([]))
    print(Solution().mergeKLists([[]]))

# Note: heapify function from the heapq module does not return a new list or the heapified list. 
# Instead, it transforms the input list in place and returns None.


# Analysis:Heap-Based Solution
# To efficiently merge k sorted linked lists, a heap-based solution leverages the properties of a priority queue, 
# specifically a min heap. This approach involves the following steps:

# The time complexity of the 'mergeKLists' method can be analyzed as follows:

# 1. Initialization of the Priority Queue (Heapify):
# • We start by filtering out the non-null heads of the linked lists and adding them to the priority queue 'pq'.
# • This initialization takes O(k) time, where k is the number of linked lists. Building a heap from these k elements using 'heapify' also takes O(k) time.

# 2. Processing Nodes:
# • We repeatedly pop the smallest element from the heap, which takes O(log k) time, as the heap contains at most k elements at any time.
# • For each node that is popped, we might push its next node into the heap, which also takes O(log k) time.
# • Since we will process each node exactly once and there are a total of N nodes across all lists, this part will take O(N log k) time.

# Combining these parts, the overall time complexity is:
# 0(k) + 0(N log k) = 0(N logk)
# Therefore, the time complexity of the 'mergeKLists' method is ON log k), where N is the total number of nodes across all k linked lists.


# Space Complexity: The space complexity is O(k) because the heap size does not exceed k, the number of linked lists.


# Example
# Consider merging three linked lists with a total of n nodes. 
# The smallest node from each list is initially added to the heap.
# When a node is polled from the heap, its successor (if any) is added to the heap.
# This process ensures that at every step, the heap helps us find the next smallest node to be added to the merged list.

# Conclusion
# The heap-based solution for merging k sorted linked lists is efficient and elegant, leveraging the min heap’s properties to ensure that the merged list is sorted with optimal time and space complexity. 
# This method stands out for its ability to handle multiple lists simultaneously while maintaining a manageable heap size.





#Approach1:Divide and Conquer

#Use the below one to write divide & conquer in interviews
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        K = len(lists)
        if K==0:
            return None
        if K==1:
            return lists[0]
        if K==2:
            return self.mergeTwoLists(lists[0],lists[1])
        mid = K//2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.mergeTwoLists(left,right)

    def mergeTwoLists(self,l1,l2):
        dummy =ListNode(-1)
        curr = dummy
        while l1 and l2:
            if l1.val<=l2.val:
                curr.next = l1
                l1=l1.next
            else:
                curr.next = l2 
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next  


# The initial approach one might consider is to merge the linked lists two at a time. 
# That is, first merge the first two lists, then merge the result with the third list, and continue this process until the kth list. 

# While this approach is theoretically sound, it proves to be inefficient for passing online judgment (OJ) systems due to its higher time complexity. 
# Therefore, a shift in strategy is essential, leading us to adopt the Divide and Conquer method.

# In essence, this method involves repeatedly dividing the task into smaller, more manageable chunks. Specifically, the k linked lists are initially divided into tasks of merging k/2 pairs of linked lists. 
# This process continues recursively, dividing the lists until we are left with tasks that involve merging only one or two linked lists, at which point the actual merging begins.

# Big-O analysis
# TC:O(nlogk)
# SC:O(n)

# • We can merge two sorted linked list in O(n) time where n is the total number of nodes in two lists.
# • Sum up the merge process and we can get: sum all nodes logk times (height of tree) => O(Nlogk)



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#Basic/Intial Solution 
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        for i in range(n - 1): # this is O(N) times of merge, while if use divide-mid-merge then it's O(logN) times of merge
            lists[i + 1] = self.mergeTwoLists(lists[i], lists[i + 1])
        return lists[-1]

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next


#Divide & Conquer
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None or len(lists) == 0:
            return None
        return self.mergeKListsHelper(lists, 0, len(lists) - 1)
    
    def mergeKListsHelper(self, lists: List[Optional[ListNode]], start: int, end: int) -> Optional[ListNode]:

        if start == end:
            return lists[start]

        mid = int((start + end) / 2)

        left = self.mergeKListsHelper(lists, start, mid)
        # print(left)

        right = self.mergeKListsHelper(lists, mid + 1, end)
        # print(right)

        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next



