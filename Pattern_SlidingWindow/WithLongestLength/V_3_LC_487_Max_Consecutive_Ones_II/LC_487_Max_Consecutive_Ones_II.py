#Approch:Sliding Window using two pointer
#TC:O(N)
#SC:O(1)
'''
We can iterate through the array, using a variable `cnt`(here zeros_cnt) to record the current number of 0s in the window. 
When cnt>k, here k =1, we move the left boundary of the window to the right by one position.

After the iteration ends, the length of the window is the maximum number of consecutive 1s.

Note that in the process above, we do not need to loop to move the left boundary of the window to the right. 
Instead, we directly move the left boundary to the right by one position. 
This is because the problem asks for the maximum number of consecutive 1s, so the length of the window will only increase, not decrease. 
Therefore, we do not need to loop to move the left boundary to the right.

The time complexity is O(n), where n is the length of the array. The space complexity is O(1).
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0 
        zeros_cnt = 0
        k =1         #maximum no of zeros that can be flipped(i.e at most one 0's), here k is not given as input
        
        l = 0
        for r in range(len(nums)):
            if nums[r]==0:
                zeros_cnt+=1
            
            while zeros_cnt>k:
                if nums[l]==0:
                    zeros_cnt-=1
                l+=1
            ans = max(ans,r-l+1)            # max-check every for iteration
            
        return ans
    
    
    


    
#Follow-up:Generalize to k maxZeros

'''
In follow-up scenarios where direct access to prior elements via nums[left] may not suffice or be efficient, an alternative approach is advocated:

Zeroes Position Queue:
Maintain a queue to record the positions of encountered zeroes. 
This queue becomes instrumental in precisely determining the next position to which the left boundary should shift when the window needs to exclude a zero to adhere to the k flips constraint.
This queue-based approach ensures that adjustments to the window’s left boundary are made with full knowledge of zeroes’ positions, thus optimizing window adjustments and maintaining the integrity of the k flips constraint.
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        zeros_cnt = 0
        k =1            #max one zero flip
        
        l =0
        q = deque()
        for r in range(len(nums)):
            if nums[r]==0:
                q.append(r)
            if len(q)>k:
                l = q.popleft()+1
            
            ans = max(ans,r-l+1)
            
        return ans
    


#Follow up: maxZeros == 1

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        lastZeroIndex = -1
        l = 0
        
        for r in range(len(nums)):
            if nums[r]==0:
                l = lastZeroIndex + 1
                lastZeroIndex = r 
                
            ans = max(ans,r-l+1)
            
        return ans

                
            
        