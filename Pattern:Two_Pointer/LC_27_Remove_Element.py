#Approach:Two pointer Algorithm
#We can use two pointer A and B.We can go through each element in the list which is indicated by pointer A.
#The first time we encounter the target value to be removed (which can be check by comparing the current value with the target value ), we assign it to the array 
# at pointer B ,then we increment the pointer B

class Solution:
    def removeElement(self,nums,val):
        etr_idx=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[etr_idx]=nums[i]
                etr_idx+=1
        return etr_idx