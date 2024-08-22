## Algorithm to Verify a Max Heap

# A max heap is a binary tree that a parent is always bigger than its children.
# A min heap is the opposite that the parent is smaller than the children.
# A heap is a complete binary tree each level is fulfilled except the last/lowest level which should be partially ful-filled from left to right.We can store the heap in a list/array

# The left index of a parent is `2*i+1` and the right index of a parent is `2*i+2`


class Solution
    def verifyMaxHeap(self,nums):
        n = len(nums)
        for i in range(n//2):
            if 2*i+1 <n and nums[i]<nums[2*i+1]:
                return False
            if 2*i+2 <n and nums[i]<nums[2*i+2]:
                return False
        return True


# The time complexity is O(N) and space complexity is O(1) constant.