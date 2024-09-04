'''
Answer to Problem 2
'''

# Definition for a Node.
class Node:
    def __init__(self, x, next = None, prev = None):
        self.val = x
        self.next = next
        self.prev = prev


'''
This recursive function would
- Create new copies.
- Assign the prev pointers in the forward step.
- Assign the next pointers in the backtracking step.
'''
def recursive_copy(node, prevNode):
    if node is None:
        return node
   
    # Create a new node
    newNode = Node(node.val)
    # Assign the prev pointer to what we get from the previous recursion step.
    newNode.prev = prevNode

    # The new nodes next pointer would point to the node returned from next recursion
    # i.e. the next new node.
    newNode.next = recursive_copy(node.next, newNode)

    return newNode

'''
copy_list function is used to copy a Linked List
The input parameter `head` is the head of the Linked List to be copied.
'''

def copy_list(head):
    return recursive_copy(head, None)