#Approach: Merge Sort using Divide & Conquer
#TC:O(nlogn)
#SC:O(n)

class Solution:
    def sortArray(self,nums):
        if len(nums)<=1:    #terminal case
            return nums

        n = len(nums)
        mid = n // 2
        first = self.sortArray(nums[:mid])
        second = self.sortArray(nums[mid:])
        return self.mergeTwoSortedArray(first,second)


    def mergeTwoSortedArray(self,a:List[int],b:List[int])-> List[int]:
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





#Approach: QuickSort Using Recursion
#TC:O(nlogn)[Best]--->O(nlogn)[Average]---->O(n^2)(Worst)
#SC:O(log(n))
import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        
        pivot = random.choice(nums)
        
        eq = [num for num in nums if num==pivot]
        smaller = [num for num in nums if num<pivot]
        bigger=[num for num in nums if num>pivot]
        
        return self.sortArray(smaller)+ eq + self.sortArray(bigger)