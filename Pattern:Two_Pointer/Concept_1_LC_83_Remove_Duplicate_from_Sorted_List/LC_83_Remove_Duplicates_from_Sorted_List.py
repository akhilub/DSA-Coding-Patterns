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


#Define head for the LList
head = ListNode(1)
p = head

#Create the LList
for i in range(2,7):
    p = p.addNode(i)

#Add a duplicate node
p = p.addNode(6)

for i in range(7,13):
    p = p.addNode(i)


#Add another duplicate node
p.addNode(12)

ListNode().printLList(head)




#Approach :Using Two Pointer
#As the linked list contains the sorted numbers, we can traverse through the linked list 
#and compare the current value and its next one if there is any,delete the next node if the next node is 
#same as current(duplicate value) by pointing the current.next to current.next.next
#TC:O(N) 
#SC:O(1)
class Solution:
    def deleteDuplicates(self,head):
        if head is None:
            return None
        curr =head
        while curr and curr.next:
            if curr.val ==curr.next.val:
                
                curr.next = curr.next.next
                
            else:
                curr = curr.next
        return head

result = Solution().deleteDuplicates(head)

ListNode().printLList(result)






# We can remove the next node using the del keyword
# node =curr.next #save the next node to delete
# curr.next = curr.next.next
# del node #delete the node


#Approach 2 :Using HashSet 

# We can use a hash set to remember the nodes that we have visited and remove the duplicate nodes
# along the way when we traverse the linked list.This approach can also be applied to the general case
# when the linked list is not sorted

#TC: O(N) 
#SC :O(N) since we are using a hash set

class Solution:
    def deleteDuplicates(self,head):
        if not head:
            return None
        prev = None
        cur = head
        seen = set()
        while cur:
            if cur.val is seen:
                node =cur
                prev.next=cur.next
                del node
            else:
                seen.add(cur.val)
                prev = cur
            cur = cur.next
        return head


