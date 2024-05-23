#Approach 1: USING A LIST TO SIMULATE THE ARRAY ROTATION
#The most basic method is to simulate as we are told. Each rotation removes one element from the end of the array and insert it to the front. The following time complexity is O(KN) because there are K rotation (where K is modulus by N) and each insert-to-front takes O(N) time.

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n 
        for i in range(k):
            x = nums.pop()
            nums.insert(0,x)
        return nums


#Approach 2:USING A DOUBLE ENDED QUEUE TO ROTATE MORE EFFICIENTLY
#If it is a double-ended queue, then inserting to the front is O(1) constant. However, we may need to copy to/from the additional deque which takes O(N) time (as we need to convert array to deque and convert it back). 
#The overall time complexity is O(N + K + N) which is still O(N) as K is less or equal to N after we do “k %= n”

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        q = deque(nums[:])
        n = len(nums)
        k=k % n
        for i in range(k):
            x = q.pop()
            q.appendleft(x)
        nums[:] = list(q)
        return nums

#Approach 3:REVERSE SUB ARRAYS TO ROTATE
#We can reverse the array once, then reverse the first K elements, and then reverse the last N-K elements. The time complexity is O(N).

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverseList(arr,l,r):
            while l<r:
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
                r-=1
            return arr
        
        n = len(nums)
        k = k%n
        reverseList(nums,0,n-1) #Reverse the entire array.
        reverseList(nums,0,k-1) #Reverse the first elements.
        reverseList(nums,k,n-1) #Reverse the last n-k elements


#Pythonic way /Competative Programming way
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        nums[k:],nums[:k] = nums[-k:],nums[:-k]


#nums[start:end:step]

#Rotating the list using slicing:
#1)nums[:-k] gives us the list excluding the last k elements. In this case, nums[:-3] results in [1, 2, 3, 4].
#2)nums[-k:] gives us the last k elements of the list. In this case, nums[-3:] results in [5, 6, 7].
#3)The assignment nums[k:], nums[:k] = nums[:-k], nums[-k:] reassigns the sliced parts back to the list in a rotated manner:
# - nums[k:] (i.e., the portion from index k to the end) is replaced with nums[:-k] (i.e., [1, 2, 3, 4]).
# - nums[:k] (i.e., the portion from the beginning to index k) is replaced with nums[-k:] (i.e., [5, 6, 7]).

#Resulting list after the operation:

#- Before the assignment: nums = [1, 2, 3, 4, 5, 6, 7].
#- After the assignment: nums = [5, 6, 7, 1, 2, 3, 4].

    
