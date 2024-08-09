#Approach: Two Pointers: one input , same end

# We use two pointers 𝑖 and 𝑗, where pointer 𝑖 points to the end of the sequence that has been processed, and pointer 𝑗 points to the head of the sequence to be processed.
# Initially, 𝑖 = −1.

# Next, we traverse 𝑗 ∈ [0,𝑛), if 𝑛𝑢𝑚𝑠[𝑗] ≠ 0  then we swap the next number pointed by pointer 𝑖 with 𝑛𝑢𝑚𝑠[𝑗] and move 𝑖 forward. 
# Continue to traverse until 𝑗 reaches the end of the array, all non-zero elements of the array are moved to the front of the array in the original order, and all zero elements are moved to the end of the array.

# The time complexity is 𝑂(𝑛), where 𝑛 is the length of the array 𝑛𝑢𝑚𝑠. The space complexity is 𝑂(1)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, n = -1 , len(nums)
        for j in range(n):
            if nums[j]!=0:
                i+=1
                nums[i],nums[j]= nums[j],nums[i]

        
