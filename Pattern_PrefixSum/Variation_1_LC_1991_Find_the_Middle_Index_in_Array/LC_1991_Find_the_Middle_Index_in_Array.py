#Approach:PrefixSum
#TC:O(n)
#SC:O(1)

#We can apply the prefix sum algorithm to this problem. We need to sum all numbers in O(N) linear time using the sum function. Then we accumulate the sum of left part – and then check the rest excluding the value at middle index.
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix = 0
        suffix = sum(nums)

        for i , v in enumerate(nums):
            suffix-=v
            if prefix ==suffix:
                return i
            prefix+=v
    return -1


