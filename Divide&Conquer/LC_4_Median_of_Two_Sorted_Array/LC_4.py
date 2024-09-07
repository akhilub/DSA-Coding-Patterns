#Write this in interviews, The way it is written

#Algorithm:Divide & Conquer
#TC:O(log(m+n))

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findKth(i1:int,i2:int,k:int)->int:
            if i1>=l1:
                return nums2[i2+k-1]
            if i2>=l2:
                return nums1[i1+k-1]
            if k==1:
                return min(nums1[i1],nums2[i2])
            
            mid = k//2
            
            midVal1 = nums1[i1+mid-1] if i1+mid-1<l1 else math.inf
            midVal2 = nums2[i2+mid-1] if i2+mid-1<l2 else math.inf
            
            return findKth(i1+mid,i2,k-mid) if midVal1<=midVal2 else findKth(i1,i2+mid,k-mid)
    
        
        l1 , l2 = len(nums1),len(nums2)
        
        # Division a // b :  floordiv(a, b)
        
        N1 = (l1+l2+1)//2         #N1 - (l1+l2+1)/2 -th number
        N2 = (l1+l2+2)//2         #N2 - (l1+l2+1)/2 -th number
        
        K1 = findKth(0,0,N1)    #K1 - kth smallest number in the interval [0,N1)
        K2 = findKth(0,0,N2)    #K2 - kth smallest number in the interval [0,N2)

        return (K1+K2)/2        #median





#Approach for The overall run time complexity should be O(log(m+n))
#Algorithm: Divide & Conquer


'''
The problem requires the time complexity of the algorithm to be O(log(m+n)), 
so we cannot directly traverse the two arrays, but need to use the binary search method.

If m+n is odd, then the median is the `(m+n+1)//2` -th number
If m+n is even,then the median is the average of the `(m+n+1)//2`-th number and the `(m+n+2)//2`-th number

In fact, we can unify it as the average of the `(m+n+1)//2`-th and `(m+n+2)//2`-th numbers


Therefore, we can design a function  
f(i,j,k), which represents the  k-th smallest number in the interval [i,m) of array `nums1` 
and the interval [j,n) of array `nums2`. 

The median is the average of f(0,0,(m+n+1)//2) and f(0,0,(m+n+2)//2)

The implementation idea of the function f(i,j,k) is as follows:

•If i≥m, it means that the interval [i,m) of array `nums1` is empty, so directly return nums2[j + k -1];
•If j≥n, it means that the interval [j,n) of array nums2 is empty, so directly return nums1[i+k-1];
•If k==1, it means to find the first number, so just return the minimum of nums1[i] and nums2[j];
•Otherwise, we find the `(k//2)`-th number in the two arrays, denoted as `midVal1` and `midVal2`.
(Note, if a certain array does not have the `(k//2)`-th number, then we regard the `(k//2)`-th number as +∞.) 

Compare the size of x and y:
• If `midVal1` ≤ `midVal2`, it means that the `(k//2)`-th number of array `nums1` cannot be the k-th smallest number, so we can exclude the interval 
[i,i+(k//2)) of array nums1, and recursively call f(i+(k//2),0,k-(k//2))


• If `midVal1` > `midVal2`, it means that the `(k//2)`-th number of array `nums2` cannot be the k-th smallest number, so we can exclude the interval 
[j,j+(k//2)) of array nums2, and recursively call f(i,j+(k//2),k-(k//2))

The time complexity is O(log(m+n)), and the space complexity is O(log(m+n)). Here, m and n are the length of arrays nums1 and nums2 respectively.
'''



class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findKth(i:int,j:int,k:int)->int:
            if i>=m:
                return nums2[j+k-1]
            if j>=n:
                return nums1[i+k-1]
            if k==1:
                return min(nums1[i],nums2[j])
            
            mid = k//2
            
            midVal1 = nums1[i+mid-1] if i+mid-1<m else math.inf
            midVal2 = nums2[j+mid-1] if j+mid-1<n else math.inf
            
            return findKth(i+mid,j,k-mid) if midVal1<=midVal2 else findKth(i,j+mid,k-mid)
    
        
        m , n =len(nums1),len(nums2)
        
        # Division a // b :  floordiv(a, b)
        
        N1 = (m+n+1)//2         #N1 - (m+n+1)/2 -th number
        N2 = (m+n+2)//2         #N2 - (m+n+2)/2 -th number
        
        K1 = findKth(0,0,N1)    #K1 - kth smallest number in the interval [0,N1)
        K2 = findKth(0,0,N2)    #K2 - kth smallest number in the interval [0,N2)

        return (K1+K2)/2        #median
    



#My Second Approach
#TC:O(m+n)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m_arr =self.mergeTwoSortedArray(nums1,nums2)  # m_arr --> mergedSortedArray
        l ,r =0,n-1
        mid = (l+r)//2
        if n&1:
            med = m_arr[mid]
        else:
            med = (m_arr[mid]+m_arr[mid+1])/2
        return med
        
    def mergeTwoSortedArray(self,a:List[int],b:List[int]):
        i, j , la,lb = 0,0,len(a),len(b)
        res = []
        while i<la and j <lb:
            if a[i]<b[j]:
                res.append(a[i])
                i+=1
            else:
                res.append(b[j])
                j+=1
        if i<la:
            res+=a[i:]
        if j<lb:
            res+=b[j:]
            
        return res







#My First Approach
#Intution
#TC:O((m+n)log(m+n))
#SC:O(m+n)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        m_arr=sorted(nums1)
        
        n =len(m_arr)
        
        l, r =0,n-1
        
        mid = (l+r)//2
        
        if n&1: #n is odd
            med = m_arr[mid]
        else:
            med = (m_arr[mid]+m_arr[mid+1])/2
            
        return med