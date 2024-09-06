'''
Answer to Problem 1
'''
# Definition for a Node.
class Node:
    def __init__(self, x, next = None):
        self.val = x
        self.next = next


# copy_list function is used to copy a Linked List
# The input parameter `head` is the head of the Linked List to be copied.
def copy_list(head):
    if head is None:
        return head
    
    # Create a new node
    newNode = Node(head.val)
    # The new nodes next pointer would point to the node returned from recursion
    # i.e. the next new node.
    newNode.next = copy_list(head.next)
    
    return newNode


