# ALGORITHM TO INSERT A NODE INTO A LINKED LIST
# The node to insert may become a new head – thus we can create a dummy head and returns the next if necessary. The first step is to locate the place to insert, and we need to store its previous Node, so that we can redirect its next pointer to the newly created node.



class ListNode:
    def __int__(self,val,next=None):
        self.val = val
        self.next= next

class Solution:
    def insertNodeLinkedList(self,head,val,pos):
        if not head:return ListNode(val)
        prev = dummy = ListNode(0,head)
        for _ in range(pos):
            prev = head
            head = head.next
        prev.next = Node(val)
        prev.next.next = head
        
        return dummy.next





# Time complexity is O(N) as we are going through the nodes once. And the space complexity is O(1) constant.