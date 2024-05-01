#Approach :Two Pointer

#TC :O(n)
#SC :O(1)
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
