class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix , suffix = 0 , sum(nums)
        for i , v in enumerate(nums):
            suffix-=v
            if prefix ==suffix:
                return i
            prefix+=v
        return -1