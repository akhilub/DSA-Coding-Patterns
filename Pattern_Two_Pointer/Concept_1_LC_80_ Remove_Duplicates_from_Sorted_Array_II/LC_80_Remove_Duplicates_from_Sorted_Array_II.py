#Approach:Two Pointers
#TC:O(n)
#SC:O(1)

'''
We use a variable `k` to record the current length of the array that has been processed.
Initially, `k` = 0, representing an empty array.

Then we traverse the array from left to right. 
For each element `x` we traverse, if `k`<2 or x ≠ nums[k-2], we put x in the position of nums[k], and then increment `k` by 1. 
Otherwise, `x` is the same as nums[k-2], we directly skip this element. Continue to traverse until the entire array is traversed.

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
        k=0
        for i in range(len(nums)):
            if k<2 or nums[k-2]!=nums[i]:
                nums[k] = nums[i]
                k+=1
        return k