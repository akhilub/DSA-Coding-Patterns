# Follow up Question:Could you do this in one pass?
# Approach Fast and Slow pointers

# We define two pointers `fast` and `slow`,both initially pointing to the dummy head node of the linked list.

# Next, the`fast`pointer moves forward `n` steps first, then`fast`and `slow` pointers move forward together until the`fast`pointer reaches the end of the linked list. At this point, the node pointed to by `slow` next is the predecessor of the 
# n-th node from the end, and we can delete it.

# The time complexity is 𝑂(𝑛) where 𝑛 is the length of the linked list. The space complexity is 𝑂(1).

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        fast = slow = dummy
        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            slow, fast = slow.next,fast.next
        slow.next = slow.next.next

        return dummy.next



#My Approach: 
#TC:O(N)
#SC:O(1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Calculate length
        tail , length = head,0
        while tail:
            length+=1
            tail = tail.next

        #Use a dummy node to handle edge cases, such as removing the head of the list.
        dummy = ListNode(0,head)
        curr = dummy

        # Find the node just before the one we want to remove
        for _ in range(length-n):
            curr = curr.next
        
        #Remove the connection(nth node from the end)
        if curr.next:
            curr.next = curr.next.next

        return dummy.next