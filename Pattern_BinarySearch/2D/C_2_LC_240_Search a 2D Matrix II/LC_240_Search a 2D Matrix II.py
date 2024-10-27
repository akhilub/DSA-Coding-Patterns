#Approach1:
#TC:mlog(n) where m is no of array and n is the no of elements in each array
#SC:O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(arr,T):
            l,r=0,len(arr)-1
            while l<=r:
                mid = (r+l)//2 or # floor((r+l)/2) or (l+r)>>1 or (r-(r-l)//2)
                if arr[mid]==target:
                    return True
                
                if arr[mid]>target:
                    r=mid-1
                else:
                    l=mid+1

            return False

        for arr in matrix:
            if binarySearch(arr,target):
                return True
        return False


#Approach2:
# Start Seach from bottom-left corner
#TC:O(m+n)
#SC:O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m , n = len(matrix) , len(matrix[0])
        row = m-1
        col = 0
        while row>=0 and col<n:
            if matrix[row][col]==target:
                return True

            if matrix[row][col]>target:
                row-=1 # all numbers in that row are even larger
            else:#matrix[row][col]<target
                col+=1 # all numbers in this row from current position col are smaller

        return False
