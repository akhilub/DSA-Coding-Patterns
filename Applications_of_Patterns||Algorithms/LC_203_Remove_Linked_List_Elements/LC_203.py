#Approach:

# Time: O(n)
# Space: O(1)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        curr=dummy
        while curr.next:
            nextNode = curr.next
            if nextNode.val==val:
                curr.next=nextNode.next
                #del nextNode                   #optional
            else:
                curr=curr.next
                
        return dummy.next