#Approach:PrefixSum

#Using Two arrays
# To solve this problem efficiently without using division, we’ll use two additional arrays.
# First, we'll create a left product array “from_left” where each element at index i represents the product of all elements to the left of nums[i].
# Then, we'll create a right product array “from_right” where each element at index i represents the product of all elements to the right of nums[i].
# Finally, we'll compute the result array “res” by multiplying corresponding elements from “from_left” and “from_right”.
# Time complexity of this solution is O(n).

#TC:O(n)
#SC:O(n)

class Solution: # 2 extra arrays
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n

        #Initialize left product array
        from_left = [1]*n
        # Product from index=0 to index=i-1
        for i  in range(1,n):
            from_left[i] = from_left[i-1]*nums[i-1]
        
        #Initialize right product array
        from_right = [1]*n
        # Product from index=n-1 to current position
        for i  in range(n-2,-1,-1):
            from_right[i] =from_right[i+1]*nums[i+1] 

        #Compute answer
        for i in range(n):
            res[i] = from_left[i]*from_right[i]

        return res

"""
res = [1]*n
for i in range(n):
    res[i] = from_left[i]*from_right[i]

    ||
    ||
    ||

res = [from_left[i]*from_right[i] for i in range(n)]

"""


#Optimized Approach 

#TC:O(n)
#SC:(1)

# We define two variables left and right, which represent the product of all elements to the left and right of the current element respectively. 
# Initially, left = 1, right = 1. Define an answer array ans of length n.
# We first traverse the array from left to right, for the ith element we update ans[i] with left, then left multiplied by nums[i].
# Then, we traverse the array from right to left, for the ith element, we update ans[i] to ans|i] x right, then right multiplied by nums[i].
# After the traversal, the array `ans` is the answer.
# The time complexity is O(n), where n is the length of the array nums. Ignore the space consumption of the answer array, the space complexity is O(1).


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        ans = [1]*n
        
        #traverse the array from left to right
        left =1
        for i in range(n):
            ans[i]=left
            left = left*nums[i]
        
        #traverse the array from right to left
        right = 1
        for i in range(n-1,-1,-1):
            ans[i] = ans[i]*right
            right = right*nums[i]
            
        return ans

