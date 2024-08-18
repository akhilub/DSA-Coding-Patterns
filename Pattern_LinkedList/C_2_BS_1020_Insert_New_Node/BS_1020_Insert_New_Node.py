# ALGORITHM TO INSERT A NODE INTO A LINKED LIST
# The node to insert may become a new head – thus we can create a dummy head and returns the next if necessary. 
# The first step is to locate the place to insert, and we need to store its previous Node, so that we can redirect its next pointer to the newly created node.

class Solution:
    def insertNodeLinkedList(self,head,val,pos):
        if not head:
            return ListNode(val)
        prev = dummy = ListNode(0,head)
        for _ in range(pos):
            prev = head
            head = head.next
        prev.next = ListNode(val)
        prev.next.next = head
        
        return dummy.next


# Time complexity is O(N) as we are going through the nodes once. And the space complexity is O(1) constant.

class ListNode:
    #Defination of a Singly Linked List
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

    def addNode(self,val):
        node = ListNode(val)
        self.next = node
        return node

    def printLList(self,head):
        curr = head
        while curr:
            print(curr.val,end = "->")
            curr = curr.next
        print() #









#Driver Code/Code Start
if __name__ =="__main__":
    inputList = [1,3,5,7]
    pos = 2
    val = 9
    
    #Define head for the LList
    head = ListNode(inputList[0])
    p = head

    #Create the LList
    for ele in inputList[1:]:
        p = p.addNode(ele)
    
    #Print the Input LList
    ListNode().printLList(head)
    
    # Create an instance of Solution & call the method
    result = Solution().insertNodeLinkedList(head,val,pos)
    
    # Print the result
    ListNode().printLList(result)
    