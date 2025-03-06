#Approach:XOR
'''
To solve this problem, we can use the XOR operation. When we XOR a number with itself, the result is 0. When we XOR a number with 0, the result is the number itself.

Since every number appears twice except for one number, if we XOR all numbers together, all the pairs will cancel out (become 0), and we'll be left with the single number.

This approach has linear time complexity O(n) and uses constant extra space O(1) .
'''


#Properties of XOR

'''
The XOR operation has the following properties:

Any number XOR 0 is still the original number, i.e., x^0 = x;

Any number XOR itself is 0, i.e.,  x^x = 0;

'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans = ans^num
        return ans