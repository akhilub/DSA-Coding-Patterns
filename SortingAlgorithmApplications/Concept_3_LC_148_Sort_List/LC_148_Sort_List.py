#Approach: MERGE SORTING A LINKED LIST BY (DIVIDE AND CONQUER TECHNIQUE)


#Given a Linked List, we can find the middle of the linked list using fast and slow pointer, disconnect the linked list at the middle point to make two sub linked lists. Recursively sort them and merge two linked list.
#Merging two sorted linked lists is quite the same as merging two sorted lists. It requires O(N+M) time. Overall, the complexity of sorting a linked list is O(NLogN).


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self,head):
        if head is None or head.next is None:
            return head
        
        
        #Get Middle Node of the LList to obtain left and right halves of the LList
        #by breaking the original LList at middle
        mid = self.getMid(head)

        # Recursively sort the right linked list
        right = self.sortList(mid)

        # Recursively sort the left linked list
        left = self.sortList(head)

        #finally merge both the Sorted LList to obtain the sorted LList
        return self.mergeTwoSortedList(left,right)


    #Using Slow and Fast Pointer Algorithm find the middle node and break the original LList at middle 
    def getMid(self,node):
        slow , fast  = node , node 
        prev = None #to break the original LList at the middle node
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next= None
        return slow
        

    #Using Merge
    def mergeTwoSortedList(self,list1,list2):
        dummy = ListNode(0)
        curr = dummy
        while list1 and list2:
            if list1.val <=list2.val:
                curr.next = list1
                list1.next = list1
            else:
                curr.next = list2
                list2.next = list2
            curr = curr.next
        curr.next = list1 or list2
        return dummy.next











#Competative Programming
#SORT LIST BY ADDITIONAL SPACE
#we can copy the linked list to a list, sort the list in O(NLogN) and iterate the linked list to overwrite the values:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def sortList(self, head):
        values = []
        node = head #copied the original LList(head) by creating another LList(node)
        
        while head:
            values.append(head.val)
            head = head.next
        
        values.sort() #sorted the list values
        values = collections.deque(values) #turned list into queue for poping out the ele from left
        head = node # copy back the node to head to put sorted array value into the original LList
        
        while head:
            head.val = values.popleft()
            head = head.next
        return node




