#TC:O(mlogn)
#SC:O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def BinarySearch(arr,target):
            l , r = 0 ,len(arr)
            while l<r:
                mid = (l+r)//2
                if arr[mid]>target:
                    r=mid
                elif arr[mid]<target:
                    l = mid+1
                else:
                    return True
            return False 


        for arr in matrix:
            if BinarySearch(arr,target):
                return True

        return False


#Approach: Search from the Bottom Left or Top Right

#Here, we start searching from the bottom left corner and move towards the top right direction. 
#We compare the current element matrix[row][col] with target:

# • If matrix [row][col] = target, we have found the target value and return true.
# • If matrix [row][col] > target, all elements to the right of the current position in this row are greater than target, so we should move the pointer row upwards/left, i.e., row = row — 1.
# • If matrix[row][col] < target, all elements above the current position in this column are less than target, so we should move the pointer col to the right, i.e., col = col+ 1.
# If we still cant find target after the search, return false.

# The time complexity is O(m + n), where m and n are the number of rows and columns of the matrix, respectively. 
# The space complexity is O (1).



class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m , n = len(matrix),len(matrix[0])
        
        row , col = m-1,0
        while row>=0 and col<n:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col]>target:
                row-=1
            else: #matrix[row][col]<target
                col+=1
                
        return False


#Optimised Solution:
#Binary Search
# We can logically unfold the two-dimensional matrix and then perform binary search.
# The time complexity is O (log(m x n)), where m and n are the number of rows and columns of the matrix, respectively. The space complexity is O (1).

#Go with this in interviews
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m , n = len(matrix),len(matrix[0])
        left ,right = 0 , m*n-1
        while left<=right:
            mid = (left+right)//2  # mid = (left+right)>>1
            # note: divide column count
            i , j = mid//n, mid%n  # i , j = divmod(mid,n)  #To get the row and column of the midpoint in the matrix, we use the divmod function with mid and n. The divmod function takes two numbers and returns a pair of numbers (a tuple) consisting of their quotient and remainder.
            if matrix[i][j]==target:
                return True
            
            elif matrix[i][j]<target:
                left= mid+1
            else:
                right= mid-1
        return False




#Just another way of writing Binary Search
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m , n = len(matrix),len(matrix[0])
        left ,right = 0 , m*n
        while left<right:
            #crucial steps
            mid = (left+right)//2  # mid = (left+right)>>1
            i , j = mid//n, mid % n #To get the row and column of the midpoint in the matrix


            if matrix[i][j]==target:
                return True
            
            if matrix[i][j]<target:
                left= mid+1
            else:
                right= mid
        return False



