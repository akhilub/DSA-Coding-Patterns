#Approach:Two pointer Algorithm
#TC:O(n)
#SC:O(1)

'''
We use the variable k to record the number of elements that are not equal to val.

Traverse the array nums, if the current element x is not equal to val, 
then assign x to nums[k], and increment k by 1.

Finally, return k.

The time complexity is O(n) and the space complexity is O(1), where n is the length of the array nums.
'''


class Solution:
    def removeElement(self,nums,val):
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        return k
    
    

#We can use two pointer A and B.We can go through each element in the list which is indicated by pointer A.
#The first time we encounter the target value to be removed (which can be check by comparing the current value with the target value ), we assign it to the array 
# at pointer B ,then we increment the pointer B
#TC:O(N)
#SC:O(1)