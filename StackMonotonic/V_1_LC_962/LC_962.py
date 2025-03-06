#Approach: Monotonic Stack
#TC:O(N)
#SC:O(N)



class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ans = 0
        stk = []
        n = len(nums)

        for i in range(n):
            if stk ==[] or nums[i]<=nums[stk[-1]]:
                stk.append(i)

        for j in range(n-1,-1,-1):
            while stk and nums[stk[-1]]<=nums[j]:
                ans = max(ans,j-stk.pop())

        return ans
    
 
 
 
    
#Using Sorting
#TC:O(nlogn)
#SC:O(1)
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        idx = sorted(map(lambda x:[x[1],x[0]], enumerate(nums)))
        ans , j = 0, len(nums)
        for _ , i in idx:
            ans = max(ans,i-j)
            j = min(j,i)
        return ans
    


'''
Syntax of the map() function
map(function, iterable)
'''


'''
idx = sorted(map(lambda i, v: [i,v], nums, range(nums.__len__())))
                            ||
                            ||
                            ||
idx = sorted(map(lambda x:[x[1],x[0]], enumerate(nums)))
                            ||
                            ||
                            ||
idx = sorted(map(lambda x: [x[1], x[0]], zip(range(len(nums)), nums)))

'''