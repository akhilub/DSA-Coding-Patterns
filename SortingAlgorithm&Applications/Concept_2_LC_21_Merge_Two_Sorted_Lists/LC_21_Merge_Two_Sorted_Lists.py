# Approach: Iteration

# We can use iteration to implement the merging of two sorted linked lists.

# First, we define a dummy head node `dummy`, then loop through the two linked lists, compare the head nodes of the two linked lists, add the smaller node to the end of 
# `dummy`, until one of the linked lists is empty, then add the remaining part of the other linked list to the end of `dummy`.

# Finally, return `dummy.next`

# The time complexity is O(m+n) where m and n are the lengths of the two linked lists respectively. Ignoring the space consumption of the answer linked list, the space complexity is O(1)


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next=list2
                list2.next = list2
            curr = curr.next
        curr.next = list1 or list2
        return dummy.next


"""
        curr.next = list1 or list2

better than:

        if list1:
            curr.next = list1
        if list2:
            curr.next = list2

"""

