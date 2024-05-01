#Appraoch 1: Greedy

#We use a variable mx to maintain the farthest index that can currently be reached, initially mx = 0.
#We traverse the array from left to right. For each position  we traverse, if mx < i , 
#it means that the current position cannot be reached, so we directly return false. 
#Otherwise, the farthest position that we can reach by jumping from position i  is i + nums[i]
#, we use i + nums[i] to update the value of mx i.e mx = max(mx,nums[i]+1)
# At the end of the traversal, we directly return true.

#TC : O(N)
#SC : O(1)

class Solution:
    def canJump(self,nums):
        mx = 0
        for i in range(len(nums)):
            if mx < i:
                return False
            mx = max(mx, i + nums[i])

        return True