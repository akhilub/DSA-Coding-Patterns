# class ListNode:
#     def __init__(self,val=0,next=None):
#         self.val = val
#         self.next = next


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


# We can remove the next node using the del keyword
node =curr.next #save the next node to delete
curr.next = curr.next.next
del node #delete the node


#Approach 2 :Using HashSet 

# We can use a hash set to remember the nodes that we have visited and remove the duplicate nodes
# along the way when we traverse the linked list.This approach can also be applied to the general case
# when the linked list is not sorted

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

#TC: O(N) 
#SC :O(N) since we are using a hash set