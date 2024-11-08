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
        
    
    