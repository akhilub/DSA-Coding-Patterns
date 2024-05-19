#Approach: 


#We traverse two linked lists and at the same time, and use the variable `carry` to indicate whether there is a carry.

#Each time we traverse, we take out the current bit of the corresponding linked list, calculate the sum with the carry `carry`
#, and then update the value of the carry. Then we add the current bit to the answer linked list. If both linked lists are traversed, and the carry is 0
#, the traversal ends.

#Finally, we return the head node of the answer linked list.

#The time complexity is  O(max((M,N)), where M and N are the lengths of the two linked lists. We need to traverse the entire position of the two linked lists, and each position only needs 
#O(1) time. Ignoring the space consumption of the answer, the space complexity is O(1).

class Solution:
    def addTwoNumbers(self,l1,l2):
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry+=l1.val
                l1 = l1.next
            if l2:
                carry+=l2.val
                l2 = l2.next
            curr.next = ListNode(carry%10)
            carry = carry//10
            curr = curr.next
        return dummy.next