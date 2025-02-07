#Approach:Monotonic Stack (Increasing)
#TC:O(n)
#SC:O(n) where n is the |nums2|
#Write this in interviews
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = {}   #numToNextGreater Map              #mapping = defaultdict(lambda: -1)
        stk = []
        for num in nums2[::-1]:
            while stk and stk[-1] <= num:
                stk.pop()
            if stk:
                m[num] = stk[-1]
            stk.append(num)
        return [m.get(x, -1) for x in nums1]       #[mapping[x] for x in nums1]


#Approach:Monotonic Stack (Increasing)
#Full Expanded Code, Good for understanding
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #1.Intialization
        n = len(nums1)
        m = len(nums2)
        ans = [-1]*n 
        
        stk = []
        dic = {}
        
        #2.Process every number in nums2 from right to left
        for i in range(m-1,-1,-1):
            while stk and stk[-1]<nums2[i] : #3.For each number in nums2, while the stack is not empty and the current number is greater than the top element of the stack:
                stk.pop()                    #Pop the element from the stack 
            
            
            if stk:                         #5.if stack is not empty
                dic[nums2[i]] = stk[-1]     #add an entry to the hashmap with current number as the key and the popped element as the value.
            else:                           #if stack is empty
                dic[nums2[i]] = -1          #add an entry to the hashmap with the number as the key and -1 as the value.
            
            
            stk.append(nums2[i])            #4.Push the current number onto the stack.
        
        #6.Finally, create an output array by mapping each number in nums1 to its corresponding value in the hashmap.
        for i in range(n):
            ans[i] = dic[nums1[i]]
            
        return ans
    
    





#Approach: Monotonic Stack (Decreasing)

class Solution:
  def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
    numToNextGreater = {}
    stack = []  # a decreasing stack

    for num in nums2:
      while stack and stack[-1] < num:
        numToNextGreater[stack.pop()] = num
      stack.append(num)

    return [numToNextGreater.get(num, -1) for num in nums1]


"""
...
...
return [numToNextGreater.get(num, -1) for num in nums1]
            
            
            ||
            ||
            ||


ans = [-1]*len(nums1)
...
...
for i in range(len(nums1)):
    ans[i] = cnt.get(nums1[i],-1)

return ans 
"""