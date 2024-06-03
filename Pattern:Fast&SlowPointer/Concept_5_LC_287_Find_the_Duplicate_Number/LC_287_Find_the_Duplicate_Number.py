#Approach:Flyod's Cycle Detection Algorithm or Hare & Tortise Algorithm or Slow and Fast Pointers

#Algorithm

# 1)Initialize two pointers, tortoise and hare, both pointing to the first element of the array. Move the tortoise one step and hare two steps
# 2)Move tortoise one step forward and hare two steps forward until they meet at a common point within the cycle.
# 3)Reset one of the pointers to the start of the array and move both pointers at the same pace until they meet again; this meeting point is the entrance to the cycle, which represents the duplicate number.

#TC:O(n) ,SC:O(1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Intialize the pointers
        slow = fast = nums[0]

        #Move the pointers
        slow = nums[nums[0]]
        fast = nums[nums[nums[0]]]
        
        #Find the intersection point of the two pointers
        while slow!=fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        #Finding the entrance to the cycle
        ans = nums[0]
        
        while ans!=slow:
            slow = nums[slow]
            ans = nums[ans]
            
        return ans # This is the duplicate number 



#When modification of input array `nums` is allowed
#Approach:Cylic Sort
#TC:O(n) ; SCO(n)
class Solution:
    def findDuplicate(self,nums):
        i, n = 0 ,len(nums)
        while i < n:
            pos = nums[i]-1
            if nums[i]!=nums[pos]:
                nums[i],nums[pos] = nums[pos],nums[i]
        return nums[-1]

