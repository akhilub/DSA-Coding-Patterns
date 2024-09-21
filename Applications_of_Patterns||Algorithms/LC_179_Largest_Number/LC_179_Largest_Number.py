#Learn this problem

'''
Python inbuilt function cmp_to_key() uses a key to compare elements
'''
#Approach1

from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Build nums containing all numbers in the String format.
        for i,v in enumerate(nums):
            nums[i] = str(v)

        # Sort nums by compare function decreasingly.
        nums = sorted(nums,key = cmp_to_key(self.compareStringNumbers))

        return str(int("".join(nums)))

    """Sorted by value of concatenated string decreasingly."""
    def compareStringNumbers(self,n1:str,n2:str): #assuming n1>n2
        
        if n1+n2>n2+n1:
            return -1
        elif n1==n2:
            return 0
        else:
            return 1

        
'''
This is how to write `if elif else` block inside a lambda function


sorted(nums, key=cmp_to_key(lambda n1, n2: 
                      -1 if n1 + n2 > n2 + n1 else 
                       0 if n1 == n2 else 1))

'''



#Competative Programming
#Approach2:

from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        
        nums = sorted(nums, key=cmp_to_key(lambda n1, n2: 
                      -1 if n1 + n2 > n2 + n1 else 1))
        
        # print(nums)
        return str(int("".join(nums)))    
    
    
'''
return str(int("".join(nums)))  
            V
            V
        better than
            V
            V

return "0" if nums[0] == "0" else "".join(nums)


'''



