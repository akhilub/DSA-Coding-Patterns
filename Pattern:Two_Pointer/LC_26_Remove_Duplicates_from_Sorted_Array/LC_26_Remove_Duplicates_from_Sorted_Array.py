#Approach:Two pointer Algorithm
# We can use two pointer A(curr) and B(ele_to_remove).We go through each element in the list which is indicated by the pointer A.
# The first time a duplicate element appears in the sorted array (which can be checked by the comparing equaity with its previous element) we assign it to
# the array at the pointer B and then we increment the pointer B
#TC:O(N)
#SC:O(1)

class Solution:
    def removeDuplictes(self,nums):
        etr_idx = 0
        for i in range(1,len(nums)):
            if nums[i-1]!=nums[i]:
                nums[etr_idx]=nums[i]
                etr_idx+=1
        return etr_idx


#competitive programming Approach
#If we can use additional space, we can use a hash set to store unique value (each number including duplicates appears only once).Then we sort the number and 
#convert them to list.Finally we copy over the original array/list
#TC:O(NlogN) -- since we sort the numbers in a set (elements in a set do not have orders).
#SC:O(N) -- as we are using a set.

class Solution:
    def removeDuplictes(self,nums):
        non_duplicates = list(sorted(set(nums)))
        for i in range(len(nums)):
            nums[i] = non_duplicates[i]
        return len(non_duplicates)





            
