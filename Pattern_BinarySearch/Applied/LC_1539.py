#My Approach
#TC:O(N)
#SC:O(M) # where M is the no of missing elements
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        s = set(arr)
        res = [] #array of missing elements
        for i in range(1,arr[-1]):
            if i in s:
                continue
            res.append(i)
        
        #Case when len(res) < k
        n = len(res)
        if n<k:
            return arr[-1] + k - n
        
        
        return res[k-1]


#How to recognize to apply BS?
#array is given in stricly increasing order
#Optimised Binary Search 
#TC:log(N)
#SC:O(1)

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
        Since the array is already sorted, why not use Binary Search
        Because we can get a solution in O(logN) time using Binary Search
        """
        
        l, r = 0,len(arr)-1
        while l<=r:
            
            mid = (l+r)//2
            """
            How many elements are missing till mid?
            Ideally, mid should have element = mid + 1
            If element at mid is not mid + 1, that means there are some missing numbers before mid
            And Count of missing numbers till mid = (current element at mid - correct element at mid)
            """
            
            # If count of missing till mid is < k that means we need to look at right side of mid for kth missing
            if arr[mid] - (mid+1) < k:      #Lesson is to think how to come up with this condition!
                l = mid +1
            # Otherwise, look at the left side of mid
            else:
                r = mid -1
        # At this point, the end pointer will point to index of largest element that is smaller than kth missing
        # So kth missing = end + k + 1
        
        return r + k +1
