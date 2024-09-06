#Approach:Hash Table
# TC: O(∣nums∣+∣head∣)
# SC: O(∣nums∣)
'''

We can use a hash table `s` to store all the elements in the array `nums`. 
Then, we define a dummy node `dummy` and point it to the head node of the list `head`.

Next, we traverse the list starting from the dummy node `dummy`. 
If the value of the next node of the current node is in the hash table `s`,
we make the current node point to the next next node; otherwise, we move the current node pointer to the next node.

Finally, we return the next node of the dummy node `dummy`.

The time complexity is O(n+m), and the space complexity is O(n). 
Here, n is the length of the array `nums`, and m is the length of the list `head`.
'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1,head) #or ListNode(next=head)    #in this case the default value of node dummy is 0 and its next is pointing to head.
        numsSet = set(nums)                                # Create a set for efficient lookup of values in nums 
        curr= dummy
        while curr.next:
            nextNode = curr.next
            if nextNode.val in numsSet:
                curr.next=nextNode.next
                #del nextNode                               # optional to make code faster
            else:
                curr=curr.next
        return dummy.next