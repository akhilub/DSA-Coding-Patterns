#Approach: Merge Sort using Divide & Conquer
#TC:O(nlogn)
#SC:O(1)

class Solution:
    def sortArray(self,nums):
        if len(nums)<=1:
            return nums

        n = len(nums)
        mid = n // 2
        first = self.sortArray(nums[:mid])
        second = self.sortArray(nums[mid:])
        return self.mergeTwoSortedArray(first,second)


    def mergeTwoSortedArray(self,a,b):
        i , j, la, lb = 0 , 0 ,len(a),len(b)
        res = []
        while i < la and j < lb:
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

