# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# DELETE NODE IN LINKED LIST – BY REMOVING NEXT
# We can make current node a copy of next node, and then remove next:


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        N = node.next
        node.val = N.val
        node.next = N.next
        del N

# This takes O(1) constant time.



# DELETE NODE IN LINKED LIST – BY SHIFTING
# We can shift node values and delete the last node:

class Solution:
    def deleteNode(self, node):
        prev = None
        while node.next:
            node.val = node.next.val
            prev= None
            node = node.next
        prev.next = None
        del node

# This takes O(N) time.