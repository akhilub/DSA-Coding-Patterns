#Write this Two Pointers in interviews
'''
Since the array `nums` is already sorted in non-decreasing order, the square values of the negative numbers in the array are decreasing, and the square values of the positive numbers are increasing. 
We can use two pointers, each pointing to the ends of the array. Each time we compare the square values of the elements pointed to by the two pointers, we put the larger square value at the end of the result array.

The time complexity is O(n), where n is the length of the array `nums`. Ignoring the space consumption of the answer array, the space complexity is O(1).
'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        l , r = 0 , n-1
        while l<=r:
            L = nums[l]**2
            R = nums[r]**2
            if L>R:
                ans.append(a)
                l+=1
            else:
                ans.append(b)
                r-=1
        return ans[::-1]













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
        hs_idx = n-1         #hs_ind --> higher square index
        while l<=r:          # or while hs_idx>=0:    #Iterate until hs_idx is less than 0
            if nums[l]**2>nums[r]**2:
                res[hs_idx] = nums[l]**2
                l+=1
            else:
                res[hs_idx] = nums[r]**2
                r-=1
            hs_idx-=1
        return res
            

#(Optimized) My Approach: Another way of writing 

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l ,r = 0 ,n-1
        ans = [0]*n
        
        while n:
            n-=1                        #Note we are decrementing n first
            if abs(nums[l])>abs(nums[r]):
                ans[n] = nums[l]*nums[l]
                l+=1
            else:
                ans[n] = nums[r]*nums[r]
                r-=1
            
        return ans
            


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



