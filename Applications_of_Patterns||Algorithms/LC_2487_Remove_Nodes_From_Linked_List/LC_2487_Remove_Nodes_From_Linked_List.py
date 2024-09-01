#Approach1:Recursion

'''
Algorithm
Base Case: If head or head.next is Null, return head.
Recursive Call: Set nextNode to removeNodes(head.next).
Comparison: If head.val is less than nextNode.val, we need to remove head. Return nextNode.
Otherwise, set head to head.next and then return head.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case, reached end of the list
        if not head:
            return None
        # Recursive call
        head.next = self.removeNodes(head.next)
        
        # If the next node has greater value than head, delete the head
        # Return next node, which removes the current head and 
        # makes next the new head
        # Otherwise ,Keep the head
        return head.next if head.next and head.val<head.next.val else head
    
    
        
        
        
        
        
        

#Approach2:Monotonic Stack
#Not Required