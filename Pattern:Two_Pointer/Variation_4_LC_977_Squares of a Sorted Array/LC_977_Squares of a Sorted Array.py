#Approach : Two Pointers
#TC:O(n)
#SC:O(n)

#Since the numbers at both ends can give us the largest square, we can use two pointers starting at both ends of the input array. 
#At any step, whichever pointer gives us the bigger square, we add it to the result array and move to the next/previous number. 
#Please note that we will be appending the bigger square 
#because the two pointers are moving from larger squares to smaller squares. 
#For that, we will be inserting the squares at the end of the output array.

#Make parabola and you will see


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n  
        l , r = 0 ,n-1
        hs_idx = n-1
        while l<=r:
            if nums[l]**2>nums[r]**2:
                res[hs_idx] = nums[l]**2
                l+=1
            else:
                res[hs_idx] = nums[r]**2
                r-=1
            hs_idx-=1
        return res
            

#Another way of writing

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
       res = [0]*n
        l , r = 0 ,n-1
        
        hs_idx = n-1
        while hs_idx>=0:    #Iterate until hs_idx is less than 0
            if nums[l]**2>nums[r]**2:
                res[hs_idx] = nums[l]**2
                l+=1
            else:
                res[hs_idx] = nums[r]**2
                r-=1
            hs_idx-=1
        return res
            

#Using for loop

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n  
        l, r = 0, n - 1
        
        for hs_idx in range(n-1,-1,-1):
            if nums[l] ** 2 > nums[r] ** 2:
                res[hs_idx] = nums[l] ** 2
                l += 1
            else:
                res[hs_idx] = nums[r] ** 2
                r -= 1
        return res



        


