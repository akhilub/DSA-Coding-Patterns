#Algorithm:Two pointer 
# TC: O(n)
# SC: O(1)

# Approach
# We define two pointers `left` and `right`, which point to the first element and the last element of the array respectively. 
# Each time we calculate numbers[left] and numbers[right]. 
# If the sum is equal to the target value, return directly [left+1,right-1]. 
# If the sum is less than the target value, move `left` to the right by one position, and if the sum is greater than the target value, move 
# `right` to the left by one position.

# The time complexity is O(n), where n is the length of the array numbers. The space complexity is O(1).


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) -1
        while left <right:
            current_sum = numbers[left]+numbers[right]
            if current_sum ==target:
                return [left+1,right+1]
            if current_sum < target:
                left+=1
            else:
                right-=1
        return res