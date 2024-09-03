#Approach:Node Assignment
'''
We can replace the value of the current node with the value of the next node, and then delete the next node. 
This can achieve the purpose of deleting the current node.

Time complexity O(1), space complexity O(1).
'''

# DELETE NODE IN LINKED LIST – BY REMOVING NEXT
# We can make current node a copy of next node, and then remove next:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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