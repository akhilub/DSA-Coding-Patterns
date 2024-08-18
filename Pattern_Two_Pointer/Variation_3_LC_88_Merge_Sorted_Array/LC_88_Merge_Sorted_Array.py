#Approach 1: Two Pointer

# We use two pointers `i` and `j` pointing to the end of two arrays, and a pointer `k` pointing to the end of the merged array.

# Every time we compare the two elements at the end of the two arrays, and move the larger one to the end of the merged array. 
# Then we move the pointer one step backward, and repeat this process until the two pointers reach the start of the arrays.

#The time complexity is O(m+n), where m and n are the lengths of two arrays. The space complexity is O(1)

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1  # nums1's index (the actual nums)
        j = n-1  # nums2's index
        k = m+n-1 # nums1's index (the next filled position)
        while j>=0:
            if i>=0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k-=1
                i-=1
            else:
                nums1[k] = nums2[j]
                k-=1
                j-=1
        

#Approach 2: Competative Programming
#TC:O(nlogn)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1[:] = sorted(nums1) #copy the sorted nums1 array

# OR Pythonic way of writing

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort() #list.sort() sorts the list in-place, mutating the list indices, and returns None (like all in-place operations).