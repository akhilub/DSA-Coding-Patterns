#Approach: FindMid + Reverse List + Merge Lists

'''
We first use fast and slow pointers to find the midpoint of the linked list, 
then reverse the second half of the list, and 
finally merge the two halves.

The time complexity is O(n), where n is the length of the linked list. The space complexity is O(1).
'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def getMid(head: ListNode):
            slow , fast  = head, head 
            prev = None 
            while fast and fast.next:                       #while fast is not None and fast.next is not None:
                fast = fast.next.next
                prev = slow
                slow = slow.next
            prev.next= None
            return slow
        
        
        def reverseList(head: ListNode):
            prev = None
            curr = head
            while curr:                                     #while curr is not None:
                nextTemp = curr.next            
                curr.next = prev                
                prev = curr                     
                curr = nextTemp                 
            return prev
        
        
        def merge(l1: ListNode, l2: ListNode) -> None:
            while l2:
                nextNode = l1.next
                l1.next = l2
                l1 = l2
                l2 = nextNode
                
        #Code start        
        if not head or not head.next:                       #if head is None or head.next is None:
            return

        mid = getMid(head)
        reverse = reverseList(mid)
        merge(head, reverse)
        