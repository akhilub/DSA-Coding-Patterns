#Approach
#
#      cur          nextTemp(assigning curr.next to nextTemp)
#    --------       --------
#    |      |       |      |
#    | head |------>|      |
#    |  1   |       |  2   |
#    --------       --------
#               
#      prev          
#    --------       
#    |      |       
#    | Null |       
#    |      |       
#    --------   

#      prev          curr           nextTemp
#    --------       --------        --------
#    |      |       |      |        |       |
#    | head |       |      |------->|       |
#    |  1   |       |  2   |        |   3   |
#    ----|----       --------       ---------
#        |      
#        |        
#    --------       
#    |      |       
#    | Null |       
#    |      |       
#    --------  


#Iterative Algorithm to reverse the Linked List
#We keep updating the previous node and the current node along the linked list and reverse the link directions
#e.g pointing the current node to previous node
#TC:O(N) where N is the no of nodes in the Linked List
#SC:O(1)
class Solution:
    def reverseList(self,head):
        prev = None
        curr = head
        while curr:
            nextTemp = curr.next            #assigning curr.next to a temproary variable nextTemp
            curr.next = prev                #changing the direction / pointing it back
            prev = curr                     #}Traversing/Moving Forward in the linked list
            curr = nextTemp                 #}
        return prev
    
    #As an instance method
    def printList(self,node): # Use 'self' parameter
        temp = node
        while temp:
            print(temp.val, end = " ")
            temp = temp.next
        print()

    #As a stactic method
    # @staticmethod          # Use the @staticmethod decorator
    # def printList(,node):
    #     temp = node
    #     while temp:
    #         print(temp.val, end = " ")
    #         temp = temp.next
    #     print()

if __name__ == "__main__":
    sol = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    #Calling the instance method
    print("Nodes in original Linked List:",end = " ")
    sol.printList(head)

    #Calling the static method
    # print("Nodes in original Linked List:",end = " ")
    # Solution.printList(head)

    ans = sol.reverseList(head)
    print("Nodes in reversed Linked List:",end = " ")
    sol.printList(ans)




#Recursive Algorithm to reverse the Linked List
#We can reverse this in Recursion Manner.
#We can reverse every other nodes except the current node,then reverse the link direction
#The Recursion is tail optimised to O(N)
#SC: O(N) where N is the number of nodes in the linked list
class Solution:
    def reverseList(self,head):
        #Base Case
        if head is None or head.next is None:
            return head
        #Recursive Case
        n = self.reverseList(head.next)
        head.next.next = head
        head.next =None
        return n


#Reverse the Linked List by changing the node value
#If we are allowed to change the node values,we dont need to modify the link
#directions.We can then go through the linked list twice.The first time we copy the node values to an array , the second time we assign the node values ( in reversed order ) to each node

# class Solution:
#     def reverseList(self,head):
#         data = []
#         p = head
#         while p:
#             data.append(p.val)
#             p = p.next
#         p = head
#         while p:
#             p.val = data.pop()
#             p = p.next
#         return head


