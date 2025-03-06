


# Intuition:
# The approach used in the code is based on bitwise operations. It maintains two variables, 'ones' and 'twos', to keep track of the bits that appear once and twice, respectively.

# Approach: 
# Initialize 'ones' and 'twos' as 0.
# Iterate through each number 'num' in the input vector 'nums'.
# Update 'ones' and 'twos' using bitwise operations:
# ones = (ones ^ num) & ~twos: XOR the current number 'num' with 'ones' to toggle the bits that appear once, then perform bitwise AND with the complement of 'twos' to remove the bits that appear twice.
# twos = (twos ^ num) & ~ones: XOR the current number 'num' with 'twos' to toggle the bits that appear twice, then perform bitwise AND with the complement of 'ones' to remove the bits that appear once.
# After iterating through all the numbers, the value stored in 'ones' will be the single number that appears only once.
# Return the value of 'ones' as the result.


# Complexity:
# The time complexity of this approach is O(n), where n is the number of elements in the input vector 'nums', as we iterate through all the numbers once.
# The space complexity is O(1) since we are using a constant amount of extra space to store the variables 'ones' and 'twos'.



class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        for num in nums:
            ones ^= num & ~twos
            twos ^= num & ~ones

        return ones
