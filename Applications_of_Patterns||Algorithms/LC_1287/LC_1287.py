#Approach 3:Binary Search
#TC:O(log(n))
#SC:O(1)


'''
The values that appear at least 25% must form a continuous span with length larger than n / 4. 
So this value must be found either at the indexes of n // 4, 2 * n // 4, or 3 * n // 4.
So totally three candidates.
'''

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        candidates = [n // 4, 2 * n // 4, 3 * n // 4] #start, mid, end
        quarter = n // 4
        
        for i in candidates:
            l = bisect_left(arr, arr[i])
            r = bisect_right(arr, arr[i])
            if r - l > quarter:
                return arr[i]
        
        return -1
    
    
#Above Algorithm expanded approach

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        candidates = [n // 4, 2 * n // 4, 3 * n // 4] #start,mid,end
        quarter = n // 4
        
        def binary_search_leftmost(A: List[int],T: int):
            L = 0
            R = len(A)
            while L < R:
                m = floor((L + R) / 2)
                if A[m] < T:
                    L = m + 1
                else:
                    R = m
            return L
        
        def binary_search_rightmost(A: List[int],T: int):
            L = 0
            R = len(A)
            while L < R:
                m = floor((L + R) / 2)
                if A[m] > T: #there is a difference in these if and else conditions when finding left and rightmost target values in array
                    R = m
                else:
                    L = m + 1
            return R
        
        for i in candidates:
            l = binary_search_leftmost(arr, arr[i])
            r = binary_search_rightmost(arr, arr[i])
            if r - l > quarter:
                return arr[i]
        
        return -1




#Approach2:Doing as what said in problem
#TC:O(m) where m is no of distinct integers
#SC:O(m)

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        arr_set = set(arr)
        n = len(arr)
        for num in arr_set:
            if cnt[num]>0.25*n:
                return num
            
        return 0



#Given Solution
#TC:
#SC:O(1)

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        for i, val in enumerate(arr):
            if val == arr[i + (n >> 2)]:
                return val
        return 0
    
    
#Same above approach
class Solution:
  def findSpecialInteger(self, arr: list[int]) -> int:
    n = len(arr)
    quarter = n // 4  # or n>>2

    for i in range(n - quarter):
      if arr[i] == arr[i + quarter]:
        return arr[i]
