class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Build nums contains all numbers in the String format.
        for i,n in enummerate(nums):
            nums[i] = str(n)

        def compare(n1,n2):
            if n1+n2>n2+n1:
                return -1
            else:
                return 1

        # Sort nums by compare function decreasingly.
        nums = sorted(nums,key = cmp_to_key(compare))

        return str(int("".join(nums)))
