#Approach:Fast & Slow Pointer Algorithm

#We can use the Fast & Slow pointers method such that the fast pointer is always twice the nodes ahead of the slow pointer. This way, when the fast pointer reaches the end of the LinkedList, 
#the slow pointer will be pointing at the middle node


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow , fast = head , head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow