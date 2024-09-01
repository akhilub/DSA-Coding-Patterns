#Write this Approach in Interviews
#Approach:Two Pointers
#TC:O(n)
#SC:O(1)

'''
We use a variable `k` to record the current length of the array that has been processed.
Initially, `k` = 0, representing an empty array.

Then we traverse the array from left to right. 
For each element `x` we traverse, if `k`=0 or x ≠ nums[k-1], we put x in the position of nums[k], and then increment `k` by 1. 
Otherwise, `x` is the same as nums[k-1], we directly skip this element. Continue to traverse until the entire array is traversed.

In this way, when the traversal ends, the first `k` elements in `nums` are the answer we want, and `k` is the length of the answer.

The time complexity is O(n), and the space complexity is O(1). Here, n is the length of the array.

Supplement:

The original problem requires that the same number appears at most 2 times. We can extend it to keep at most `k` identical numbers.

•Since the same number can be kept at most `k` times, we can directly keep the first `k` elements of the original array;
•For the later numbers, the premise of being able to keep them is: the current number x compares with the `kth` element from the end of the previously kept numbers. 
 If they are different, keep it, otherwise skip it.
'''



class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums)):
            if k==0 or nums[i]!=nums[k-1]:
                nums[k]=nums[i]
                k+=1
        return k






















#Approach:Two pointer Algorithm
# We can use two pointer A(curr) and B(ele_to_remove).
# We go through each element in the list which is indicated by the pointer A.
# The first time a duplicate element appears in the sorted array (which can be checked by the comparing equaity with its previous element) we assign it to
# the array at the pointer B and then we increment the pointer B
#TC:O(N)
#SC:O(1)

class Solution:
    def removeDuplictes(self,nums):
        etr_idx = 1
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





            
