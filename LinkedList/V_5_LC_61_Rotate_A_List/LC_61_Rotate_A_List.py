#Write this in interviews

#My Approach
#TC:O(N)
#SC:O(1)

# Definition for singly-linked list
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k==0:
            return head
        
        #1. Get Length & find tail Node
        tail,length = head,1
        while tail.next:
            tail = tail.next
            length+=1
        
        #2. Circle the list (connect the tail to the head)
        tail.next = head  
        
        #3. Find Pivot
        pivot = length - k % length 
        
        for _ in range(pivot): 
            tail = tail.next
        
        #4. Rotation (Set the new head and break the cycle)
        newHead = tail.next     
        tail.next = None
        
        return newHead       
          
      



    
       































































































#Approach
#1) Find the length of the LList and the tail position
#2) Keep the rotation within the length
#3) Find the pivot position , remove the connection and stich it to the front
#TC: O(N)
#SC:O(1)

# nums = [1,2,3,4,5], k=2 places to the right  


class Solution:
    def rotateList(self,head):
        if head is None:
            return None

        #Get Length and Tail Node
        length , tail = 1, head
        while tail.next:
            tail = tail.next
            length+=1

        #Calculate the effective rotations needed
        k = k % length
        if k == 0:  #meaning no rotation or a multiple of k
            return head
        
        #Find pivot position
        pivot = length - k - 1 # -1 because we are counting length from 1
        #Move head to pivot
        cur = head #Now whatever happens with cur will be reflected to head too
        for i in range(pivot):
            cur = cur.next

        #Rotation
        newHead = cur.next  #GetSubList after pivot   4 --> 5 --> None
        cur.next = None     #Remove connection         #now   head = 1 -->2 -->3 -->None
        tail.next = head    #Stich the tail to the front    # so now tail = 5 --> 1 ---> 2 ---> 3 --->None
        
        return newHead #Now what is pointing to node 5 , node 4 which is in newHead and that is what we have to return , newHead = 4 -->5 -->1 --> 2--->3--->None





