#Approach:PrefixSum

#Using Two arrays
#TC:O(n)
#SC:O(n)

class Solution: # 2 extra arrays
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n

        from_left = [1]*n
        # Product from index=0 to index=i-1
        for i  in range(1,n):
            from_left[i] = from_left[i-1]*nums[i-1]
        
        # Product from index=n-1 to current position
        from_right = [1]*n
        for i  in range(n-2,-1,-1):
            from_right[i] =from_right[i+1]*nums[i+1] 

        for i in range(n):
            res[i] = from_left[i]*from_right[i]

        return res



#Optimized Approach 

#TC:O(n)
#SC:(1)

# We define two variables left and right, which represent the product of all elements to the left and right of the current element respectively. 
# Initially, left = 1, right = 1. Define an answer array ans of length n.
# We first traverse the array from left to right, for the ith element we update ans[i] with left, then left multiplied by nums[i].
# Then, we traverse the array from right to left, for the ith element, we update ans[i] to ans|i] x right, then right multiplied by numsli].
# After the traversal, the array `ans` is the answer.
# The time complexity is On), where n is the length of the array nums. Ignore the space consumption of the answer array, the space complexity is O(1).


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

