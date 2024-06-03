#Approach:Fast and Slow Pointer

#Given two pointers fast and slow.Fast Pointer traverse two steps at a time and slow pointer traverse one step at a time.
#If they meet somewhere , it means there is a cycle.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#TC:O(N)
#SC:O(1)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Intialize
        slow ,fast = head,head
        while fast is not None and fast.next is not None:
            slow= slow.next
            fast = fast.next.next
            #Find the intersection i.e # Check if slow and fast pointers meet (cycle detected)
            if slow ==fast:
                return True             # Found a cycle in the linked list
        return False                    # No cycle found in the linked list




#Approach : Using Hash Set
#TC:O(N)
#SC:O(1)