#Learn this problem

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Build nums containing all numbers in the String format.
        for i,v in enummerate(nums):
            nums[i] = str(v)

        # Sort nums by compare function decreasingly.
        nums = sorted(nums,key = cmp_to_key(self.compareStringNumbers))

        return str(int("".join(nums)))

    def compareStringNumbers(n1:str,n2:str): #assuming n1>n2
        """Sorted by value of concatenated string decreasingly."""
        if n1+n2>n2+n1:
            return -1
        elif n1==n2:
            return 0
        else:
            return 1
            