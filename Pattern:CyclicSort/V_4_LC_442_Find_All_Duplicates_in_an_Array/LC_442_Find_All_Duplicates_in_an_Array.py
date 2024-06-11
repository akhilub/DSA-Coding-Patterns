class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i,n=0,len(nums)
        while i <n:
            pos = nums[i]-1 # Calculate the index where the current element should be if it's not a duplicate. note `-1` because integers of nums are in the range [1, n]
            if nums[i]!=nums[pos]: # Check if the current element is not in its correct position.
                nums[pos],nums[i]=nums[i],nums[pos]  # Swap the current element with the element at its correct position.
            else:
                i=i+1 # Move to the next element if the current element is already in its correct position.
        
        duplicateNumbers = []
        for i in range(n):
            if nums[i]!=i+1: # Identify elements that are not in their correct positions, which are duplicates.
                duplicateNumbers+=[nums[i]] # Add the duplicates to the list.
                
        return duplicateNumbers