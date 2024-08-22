#Approach:Binary Search
#TC :O(log(n-k)+k)
#SC:O(k)

'''
Why Binary Search ?
Intution:because the given arr is sorted

'''
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        l ,r = 0, n-k 
        while l<r:
            mid = (l+r)//2
            if (arr[mid]+arr[mid+k])//2 < x:
                l = mid+1
            else:
                r = mid
        return arr[l:l+k]




#Competative Programming
#Approach:Sort
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr = sorted(arr,key =lambda i :abs(i-x))
        return sorted(arr[:k])
    
    
    
#Binary Search Another Way
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        l ,r =0 ,n-1-k    #First Change at r = n-1 -k
        while l<=r:       #Second Change l<=r
            mid = (l+r)//2
            if (arr[mid]+arr[mid+k])//2 < x:
                l = mid+1
            else:
                r = mid-1 #Third Change r =mid-1
        return arr[l:l+k]