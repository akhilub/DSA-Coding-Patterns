#Approach :Two Pointer



#Initially, we consider the capacity of the water that the two farthest pillars can hold. The width of the water is the distance between the two pillars, and the height of the water depends on the shorter one between the two pillars.

#The current pillars are the pillars on the farthest sides, so the width of the water is the largest. For other combinations, the width of the water is smaller. Suppose the height of the left pillar is less than or equal to the height of the right pillar, then the height of the water is the height of the left pillar. If we move the right pillar, the width of the water will decrease, but the height of the water will not increase, so the capacity of the water will definitely decrease. Therefore, we move the left pillar and update the maximum capacity.

#Repeat this process until the two pillars meet.

#The time complexity is O(n), where n is the length of the array height. The space complexity is O(1)
class Solution:
    def maxArea(self,height:List[int])->int:
        l , r = 0 , len(height) - 1
        ans = 0 
        while l < r:
            minHeight = min(height[l],height[r])
            area = (r-l)*minHeight
            ans = max(ans, area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return ans
