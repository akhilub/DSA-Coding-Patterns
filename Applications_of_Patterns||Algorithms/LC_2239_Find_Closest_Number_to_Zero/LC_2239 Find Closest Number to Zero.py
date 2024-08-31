'''
sorted_nums = sorted(nums, key=lambda x: (abs(x), -x)) is sorting the list nums based on a custom key.

1.sorted(nums, key=...): This part sorts the list nums. The key parameter is a function that extracts a comparison key from each element in nums to determine the order. In this case, the key is defined by a lambda function.

2.lambda x: (abs(x), -x): This lambda function takes each element x in the list and returns a tuple (abs(x), -x). This tuple serves as the sorting key for each element.
- abs(x): This is the absolute value of x. It ensures that the numbers are sorted by their absolute values first. For example, for nums = [2, -1, 1], the absolute values are [2, 1, 1].
- x: This is the negative of the number. It is used to handle the case where two numbers have the same absolute value. If two numbers have the same absolute value, this secondary sorting criteria ensures that the positive number appears before the negative number.

For nums = [2, -1, 1].The list of keys becomes [(2, -2), (1, 1), (1, -1)]
'''

#TC:O(NlogN)
#SC:O(1)
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums, key = lambda x: (abs(x), -x))
        return sorted_nums[0]


#Algorithmic Solution
#TC:O(N)
#SC:O(1)
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans , d = 0 , inf
        for num in nums:
            if (y:=abs(num)) < d or (y == d and num > ans):
                ans ,d = num ,y
        return ans


"""
Walrus Operator  `:=`

This symbol := is an assignment operator in Python (mostly called as the Walrus Operator). 
In a nutshell, the walrus operator compresses our code to make it a little shorter.

Here's a very simple example:

# without walrus
n = 30
if n > 10:
    print(f"{n} is greater than 10")

# with walrus
if (n := 30) > 10:
    print(f"{n} is greater than 10")
These codes are the same (and outputs the same thing), but as you can see, the version with the walrus operator is compressed in just two lines of code to make things more compact.
"""
        

