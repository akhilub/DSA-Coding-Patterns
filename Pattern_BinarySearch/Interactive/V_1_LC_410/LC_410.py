#Approach: Applied Binary  Search
#Monotonically decreasing function

'''
We notice that the larger the maximum sum of the subarrays, the fewer the number of subarrays. 
When there is a maximum sum of the subarrays that meets the condition, then a larger maximum sum of the subarrays will definitely meet the condition. 
This means that we can perform a binary search for the maximum sum of the subarrays to find the smallest value that meets the condition.


We define the left boundary of the binary search as left=max(nums), and the right boundary as right=sum(nums). 
Then for each step of the binary search, we take the middle value mid=⌊(left+right)/2⌋, 
and then determine whether there is a way to split the array so that the maximum sum of the subarrays does not exceed mid. 
If there is, it means that mid might be the smallest value that meets the condition, so we adjust the right boundary to `mid`. 
Otherwise, we adjust the left boundary to `mid+1`.


How do we determine whether there is a way to split the array so that the maximum sum of the subarrays does not exceed mid? 

We can use a greedy method, traverse the array from left to right, and add the elements of the array to the subarray one by one.
If the current sum of the subarray is greater than mid, then we add the current element to the next subarray. 

If we can split the array into no more than k subarrays, and the maximum sum of each subarray does not exceed mid, 
then mid is the smallest value that meets the condition. 
Otherwise, mid does not meet the condition.

The time complexity is O(nxlogm), and the space complexity is O(1). Here, 
n and m are the length of the array and the sum of all elements in the array, respectively.
'''



class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def f(ms):                  #ms- provided maximum sum
            s, cnt = inf , 0        #s - current sum
            for num in nums:
                s+=num
                if s>ms:
                    s = num
                    cnt+=1
            return cnt
        
        L,R = max(nums),sum(nums)       #L-minimum subarray sum ,R-maximum subarray sum
        while L<R:
            mid = (L+R)//2
            if f(mid)>k:
                L = mid+1
            else:
                R = mid
        return L