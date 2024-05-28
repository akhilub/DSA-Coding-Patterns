#Approach: Use a HashSet
#We traverse the array and record the elements that have appeared in the hash set `seen`. If an element appears for the second time, it means that there are duplicate elements in the array, and we directly return true.

#TC: O(N) ,where N is in the number of elements in the input array
#SC: O(N)


class Solution:
    def containsDuplicate(self,nums):
        seen  = set()
        for ele in nums:
            if ele in seen:
                return True
            seen.add(ele)
        return False

if __name__ == "__main__":
    sol = Solution()
    nums1 = [1,2,3,4]
    print(sol.containsDuplicate(nums1)) #Expected Output : False

    sol = Solution()
    nums2 = [1,2,3,1]
    print(sol.containsDuplicate(nums2)) #Expected Output : True

    sol = Solution()
    nums3 = [1,1,1,3,3,4,3,2,4,2]
    print(sol.containsDuplicate(nums3)) #Expected Output : False


#Approach2 : Sorting can help
#TC: O(NLogN)
#SC: 0(1) or O(N)
class Solution:
    def containsDuplicate(self,nums):
        nums.sort()
        for idx, ele in enumerate(nums[:-1]):
            if ele == nums[idx+1]:
                return True
        return False
        

#Advanced Optimized way
class Solution:
    def containsDuplicate(self,nums):
        return len(set(nums))<len(nums)
        