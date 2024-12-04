#Approach:Recursion
#TC:O(n)
#SC:O(n)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return
        tail = head
        
        for _ in range(k):
            if not tail: return head                    # if there are less than k nodes in the list, do nothing.
            tail = tail.next                            # default reach to kth Node
            
        newHead = self.reverseKList(head,tail)
        head.next = self.reverseKGroup(tail,k)
        return newHead
    
    def reverseKList(self,head:Optional[ListNode],tail:Optional[ListNode])-> Optional[ListNode]:
            """Reverses (head, tail)."""
            prev = None
            curr = head
            while curr!=tail:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            return prev
    
    
    
    
    
    
    
    
    
#Follow Up:
# TC:O(n)
# SC:O(1)


'''
To reverse a linked list in groups of size k, the process involves dividing the original linked list into several segments, each consisting of k nodes, and then individually reversing each segment. This operation necessitates two distinct functions: one for segmenting and another for reversing.

Consider the linked list 1->2->3->4->5 as an example. A common practice in linked list manipulations is to prepend a dummy node to the list. This is because the head of the list might change during the reversal process. The introduction of a dummy node ensures the head’s position is consistently trackable. Consequently, after adding a dummy node, the linked list becomes -1->1->2->3->4->5.


To reverse a group of nodes, for instance, nodes 1, 2, and 3 when k is 3, we employ two pointers: pre and next. The pre pointer indicates the node immediately preceding the group to be reversed, while next points to the node following the group. Post-reversal, the pre pointer advances to mark the new starting position for the next group reversal.

During each iteration for swapping a k-group, prev remains stationary, anchoring the start of the group being reversed, whereas current begins at node ‘1’ and moves through the group. Notably, for the duration of a single batch swap within the while (kcopy > 0) loop, prev does not shift:


```
Initial list: 1->2->3->4->5 , with k=3

After first step: 2->1->3->4->5
After full reversal: 3->2->1->4->5
Note: The 'next' node for 'prev' is continually updated to 'current’s next, hence 'current' remains unchanged in a single batch swap.
```


The time complexity is O(n), and the space complexity is O(1). Here, n is the length of the linked list.



'''



class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]: 
        '''
            for reverse 1->2->3->4->5, process is like
                1->None, 2->3->4->5
                2->1->None, 3->4->5
                3->2->1->None, 4->5
                4->3->2->1->None, 5
                5->4->3->2->1->None, None
        '''  
        dummy = ListNode(next=head)
        pre = cur = dummy
        while cur.next:
            for _ in range(k):
                cur = cur.next
                if cur is None:
                    return dummy.next
                
            t = cur.next
            cur.next = None # cut from next k-group, so to reverseList() for current k-group
            start = pre.next
            pre.next = self.reverseList(start)
            start.next = t # so now 'start' is the last node of k-group
            pre = cur = start # same as the reset dummy before while loop
        return dummy.next
    
    def reverseList(self,head):
        prev, curr = None, head
        while curr!=None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev
