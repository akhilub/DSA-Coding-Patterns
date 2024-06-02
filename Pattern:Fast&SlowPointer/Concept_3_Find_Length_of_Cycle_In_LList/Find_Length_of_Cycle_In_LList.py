class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

    def addNode(self,val):
        node = ListNode(val)
        self.next = node
        return node
    
class Solution:
    def findCycleLength(self,head):
        if head is None:
            return None
        
        slow,fast = head,head                                                    # Initialize slow and fast pointers to the head of the linked list

        while fast.next is not None and fast.next.next is not None:              # Traverse the linked list using slow and fast pointers
            slow = slow.next
            fast = fast.next.next                                                # Move fast pointer two steps at a time and slow pointer one step at a time
            
            
            if (slow==fast): # found the cycle                                   # Check if the slow and fast pointers meet, indicating the presence of a cycle
                return self.calculateCycleLength(slow)

        return 0

    def calculateCycleLength(self,slow):
        curr = slow
        length = 0

        while True:                                                              # Count the length of the cycle by moving through it
            curr = curr.next
            length+=1

            if curr ==slow:                                                      # If we reach the starting point, we have completed a full cycle
                break

        return length

if __name__== "__main__":
    head = ListNode(1)
    p = head

    for i in range(2,7):
        p = p.addNode(i)

    # Create a cycle in the linked list
    p.next = head.next.next

    #head
    #|
    #1--->2---->3---->4---->5---->6---
    #           ^                    |
    #           |____________________|                     


    sol = Solution()

    # Find and print the length of the cycle
    print("LinkedList cycle length: " + str(sol.findCycleLength(head)))

