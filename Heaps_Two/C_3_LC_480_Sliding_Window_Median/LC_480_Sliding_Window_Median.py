'''
>>> nums = [1,3,-1,-3,5,3,6,7]
>>> k = 3
>>> window = sorted(nums[:k])
>>> window
[-1, 1, 3]
>>>
>>> nums[k:] + [0]
[-3, 5, 3, 6, 7, 0]
>>> zip(nums, nums[k:] + [0])
<zip object at 0x108f384c0>
>>> list(zip(nums, nums[k:] + [0]))
[(1, -3), (3, 5), (-1, 3), (-3, 6), (5, 7), (3, 0)]
>>>
>>>
>>> window.remove(1)
>>> window
[-1, 3]

>>> bisect.insort(window, -3)
>>> window
[-3, -1, 3]
'''

'''
>>> nums
[1, 3, -1, -3, 5, 3, 6, 7]
>>>
>>> nums[1]
3
>>> nums[~1]
6
'''


#Approach: Using BuiltIn Methods

#TC:O(klogk+nk)
#SC:O(n)


import bisect
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]: # this solution is just the natural flow
        window = sorted(nums[:k])
        medians = []
        for a , b in zip(nums,nums[k:]+[0]):                # +[0] to keep the loop running
            median = (window[k//2] + window[~(k//2)])/2     # e.g. k=3 and nums[1,2,3], so it should enter the loop for one time
            medians.append(median)
            
            window.remove(a)
            bisect.insort(window,b)
        return medians
    
    
'''

~i = -1-i


window[~(k//2)]
    ||  
    ||
window[-1-(k//2)]

'''






#Appproach:Sorted list-k (Sliding Window Techinque)
#TC:O(nlogk)
'''

We first add the first `k` arrays of the array to the set. Since `multiset` has its own sorting function, we can quickly find the iterator `mid` pointing to the middle number through `k/2`.

If `k` is an odd number, then the number pointed to by `mid` which is the median;
if `k` is an even number, then the average of the number pointed to by `mid` and the `previous number` is the median.

When we add a new number to the collection, the multiset will be added to the correct position according to the size of the new number, and then we see that

• if the newly added number is smaller than the number pointed to by the previous mid, then the median must be pulled down , so mid moves forward by one,
• and if the number to be deleted is less than or equal to the number pointed to by mid (note that the equal sign is added here because the number to be deleted may be the number pointed to by mid), then mid moves backward by one.

Then we delete the leftmost number of the sliding window.


Time Complexity:

Inserting into or removing from a SortedList takes  O(logk).

Computing the median takes  O(1).

For n-k+1 windows, the overall complexity is O((n-k+1)⋅logk) ≈ O(nlogk).

'''















from sortedcontainers import SortedList
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # Initialize the sorted window with the first `k` elements
        window = SortedList(nums[:k])  
        
        medians = []
        n = len(nums)
        
        for i in range(k, n + 1):
            # Compute the median
            
            if k&1:  # Odd window size
                medians.append(window[k // 2])
            else:    # Even window size
                medians.append((window[k // 2 - 1] + window[k // 2]) / 2)
            
            # Exit loop after processing the last window
            if i == n:  
                break
            
            # Update the sliding window
            window.remove(nums[i - k])  # Remove the element going out of the window
            window.add(nums[i])         # Add the new element into the window
        
        return medians
    
    
    
    
    
    
    
    
    
    
    
#BruteForce 
#TC:O(n•klogk)

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        n = len(nums)
        arr = nums[:k-1]                #q = deque(nums[:k-1])
        ans = []
        
        for i in range(k-1,n):
            if i>k-1:
                arr.pop(0)              #q.popleft()
            
            arr.append(nums[i])         #q.append(nums[i])
            
            window = sorted(arr)        #window = sorted(q)
            
            if k&1:  # Odd window size
                ans.append(window[k // 2])
            else:    # Even window size
                ans.append((window[k // 2 - 1] + window[k // 2]) / 2)
                
        return ans