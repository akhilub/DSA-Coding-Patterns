from typing import List
from itertools import zip_longest

class SparseVector:
    def __init__(self,nums:List[int]):
        self.d = {i:v for i,v in enumerate(nums) if v}
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec:"SparseVector")-> int:
        a , b = self.d , vec.d 
        if len(b)<len(a):
            a,b = b,a 
        return sum(v*b.get(i,0) for i,v in a.items())
    
    

#My Approach
class Solution:
    def myDotProduct(self,nums1,nums2):
        ans = 0
        for v1 ,v2 in zip_longest(nums1,nums2,fillvalue = 0):
            ans += v1*v2
        return ans
        


 
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

if __name__=="__main__":
    #TestCase1
    nums1 = [1,0,0,2,3] 
    nums2 = [0,3,0,4,0]
    v1 = SparseVector(nums1)
    v2 = SparseVector(nums2)
    ans = v1.dotProduct(v2)
    print(ans)
    
    print(Solution().myDotProduct(nums1,nums2))
    
    
    #TestCase2
    nums1 = [0,1,0,0,0]
    nums2 = [0,0,0,0,2]
    v1 = SparseVector(nums1)
    v2 = SparseVector(nums2)
    ans = v1.dotProduct(v2)
    print(ans)
    
    print(Solution().myDotProduct(nums1,nums2))
    
    #TestCase3
    nums1 = [0,1,0,0,2,0,0]
    nums2 = [1,0,0,0,3,0,4]
    v1 = SparseVector(nums1)
    v2 = SparseVector(nums2)
    ans = v1.dotProduct(v2)
    print(ans)
    
    print(Solution().myDotProduct(nums1,nums2))
    
    
    
    
    
    
    
'''
zip_longest

- zip_longest takes two or more iterables as input.
- It iterates until the longest iterable is exhausted.
- If the shorter iterables are exhausted before the longest one, the missing values are filled with the fillvalue (which is None by default).


Syntax

zip_longest(*iterables, fillvalue=None)

zip_longest( iterable1, iterable2, fillvalue)




Example


from itertools import zip_longest

nums1 = [1, 2, 3] 
nums2 = [10, 20]

print(list(zip(nums1, nums2))) 
# [(1, 10), (2, 20)] 

print(list(zip_longest(nums1, nums2)))
# [(1, 10), (2, 20), (3, None)]

print(list(zip_longest(nums1, nums2,fillvalue=0)))
# [(1, 10), (2, 20), (3, 0)]


Reference 1:(https://www.educative.io/answers/what-is-the-itertoolsziplongest-module-in-python)
Reference 2:(https://www.tutorialspoint.com/python-itertools-zip-longest)

'''
    