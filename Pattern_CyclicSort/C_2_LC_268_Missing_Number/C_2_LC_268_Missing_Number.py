#Approach :Modified Cyclic Sort , since array has number ranging from 0 to n
#TC:O(n)
#SC:O(1)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i , n = 0, len(nums)
        while i < n :
            pos = nums[i]
            if nums[i] < n and nums[i]!=nums[pos]:
                nums[i],nums[pos] = nums[pos],nums[i]
            else:
                i+=1
            
        for i in range(n):
            if nums[i]!=i:
                return i
        return n


#Approach:Maths
#Using Total Sum upto n - Sum of elements of array
'''
We can also solve this problem using mathematics. By calculating the sum of [0,..n], subtracting the sum of all numbers in the array, we can obtain the missing number.

The time complexity is O(n), where n is the length of the array. The space complexity is O(1).
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        summation_n = n*(n+1)//2
        summ = sum(nums)
        return summation_n - summ






#There are many other approaches to solve this problem, No need to go for bitwise operation

'''
The XOR (exclusive OR) operation compares corresponding bits of two numbers:

0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0
'''
#Approach : Using Bit Wise Operator
#TC:O(n)
#SC:O(1)


'''
The XOR operation has the following properties:

Any number XOR with 0 is still the original number, i.e., x ^ 0 = x;
Any number XOR with itself is 0, i.e.,  x^x = 0;

Therefore, we can traverse the array, perform XOR operation between each element and the numbers [0..n], and the final result will be the missing number.
'''
class Solution:
    def missingNumber(self,nums):
        ans  = len(nums)

        for i , num in enumerate(nums):
            num = i ^ num                           #} these two lines can be condensed to 
            ans = ans ^ num                         #} ans = ans^i^num
            return ans







