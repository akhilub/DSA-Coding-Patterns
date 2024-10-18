#Approach :Two Pointers +Sorting
#TC:O(n²)
#SC:O(|ans|)

'''
We notice that the problem does not require us to return the triplet in order, so we might as well sort the array first, which makes it easy to skip duplicate elements.

Next, we enumerate the first element of the triplet nums[i], where 0≤i<n−2. For each i, we can find j and k satisfying 

nums[i]+nums[j]+nums[k]=0 by maintaining two pointers j=i+1 and k=n−1. 
In the enumeration process, we need to skip duplicate elements to avoid duplicate triplets.

The specific judgment logic is as follows:

If i>0 and nums[i]=nums[i−1], it means that the element currently enumerated is the same as the previous element, we can skip it directly, because it will not produce new results.

If nums[i]>0, it means that the element currently enumerated is greater than 0, so the sum of three numbers must not be equal to 0, and the enumeration ends.

Otherwise, we let the left pointer j=i+1, and the right pointer k=n−1. 
When j<k, the loop is executed, and the sum of three numbers x=nums[i]+nums[j]+nums[k] is calculated and compared with 0:

If x<0, it means that nums[j] is too small, we need to move j to the right.
If x>0, it means that nums[k] is too large, we need to move k to the left.
Otherwise, it means that we have found a valid triplet, add it to the answer, move j to the right, move k to the left, 
and skip all duplicate elements to continue looking for the next valid triplet.

After the enumeration is over, we can get the answer to the triplet.

The time complexity is O(n^2)and the space complexity is O(logn). The n is the length of the array.
'''



class Solution:
    def threeSum(self,nums:List[int])->List[List[int]]:
        if len(nums)<3:return ans
        
        nums = sorted(nums)
        ans = []
        n = len(nums)
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            # Choose nums[i] as the first number in the triplet, then search the
            # remaining numbers in [i + 1, n - 1].
            l , r = i+1,n-1
            while l<r:
                summ = nums[i]+nums[l]+nums[r]
                if summ==0:
                    ans.append((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                    #skip duplicates
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                    while nums[r]==nums[r+1] and l<r:
                        r-=1
                        
                elif summ <0:
                    l+=1
                else:
                    r-=1
                    
        return ans
                    







#Approach: Sorting + Two Pointers (using HashSet)
#TC:O(n²)
#SC:O(|ans|)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n = len(nums)
        nums = sorted(nums)
        for i in range(n):
            l,r = i+1,n-1
            while l<r:
                S = nums[i]+nums[l]+nums[r]
                if S == 0:
                    ans.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
                elif S > 0:
                    r-=1
                else:
                    l+=1
          
        return [list(tup) for tup in ans]
        