#Approach: Slow and Fast Pointer

#We first use the fast and slow pointers to judge whether the linked list has a cycle. 
#If there is a cycle, the fast and slow pointers will definitely meet, and the meeting node must be in the cycle.

#If there is no cycle, the fast pointer will reach the tail of the linked list first, and return `null` directly.


# If there is a cycle, we then define an answer pointer `ans`,to point to the head of the linked list, 
#and then let  `ans` and the slow pointer move forward together, moving one step at a time, 
#until `ans` and the slow pointer meet, and the meeting node is the cycle entrance node.


class Solution:
    def detectCycle(self,head):

        slow,fast= head,head
        hasCycle = False

        while not hasCycle and fast.next and fast is None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                hasCycle = True

        
        if not hasCycle:
            return 

        ans = head
        while ans!=slow:
            ans = ans.next
            slow = slow.next

        return ans




###############

class Solution:
     def detectCycle(self,head):
        #Intialize the pointers
        slow = fast = head

        #Move the pointers
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            #Find the intersection point of the two pointers
            if slow == fast:
                #Finding the entrance to the cycle
                ans = head  
                while ans!=slow:
                    slow = slow.next
                    ans = ans.next
                return ans # This is the node where cycle begins
                
            
        return None #otherwise return None