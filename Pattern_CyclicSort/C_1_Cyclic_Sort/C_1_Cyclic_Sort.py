#Approach : we iterate the array one number at a time, and if the current number we are iterating is not at the correct index, we swap it with the number at its correct index. 
#This way, we will go through all numbers and place them at their correct indices, hence, sorting the whole array.


#TC:O(n)
#SC:O(1)

#Use the while loop, do not go with `for` loop

class Solution:
    def sort(self,nums):
        i = 0
        while i < len(nums):
            j = nums[i] - 1 #Calculate the index where the current element should be place
            if nums[i]!=nums[j]: # Check if the current element is not in its correct position.
                nums[i],nums[j]=nums[j],nums[i] # Swap the current element with the one at its correct position.
            else:
                i+=1 # If the current element is already in its correct position, move to the next element.
        return nums
