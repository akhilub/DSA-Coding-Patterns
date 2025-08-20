#Approach:Monotonic Stack (Increasing)
#TC:O(N)
#SC:O(N)


'''
This problem requires us to find the position of the first element greater than each element to its right, which is a typical application scenario for a monotonic stack.


We traverse the array temperatures from right to left, maintaining a stack stk that is monotonically increasing from top to bottom in terms of temperature. The stack stores the indices of the array elements. 
For each element temperatures[i], we continuously compare it with the top element of the stack. 
If the temperature corresponding to the top element of the stack is less than or equal to temperatures[i], 
we pop the top element of the stack in a loop until the stack is empty or the temperature corresponding to the top element of the stack is greater than temperatures[i]. 
At this point, the top element of the stack is the first element greater than temperatures[i] to its right, and the distance is stk.top()−i. 
We update the answer array accordingly. Then we push temperatures[i] onto the stack and continue traversing.

After the traversal, we return the answer array.

The time complexity is O(n), and the space complexity is O(n). 
Here, n is the length of the array temperatures.
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stk = []                                                # Initialize an empty stack to store indices of temperatures.
        ans = [0]*n                                             # Initialize a result list with zeros.
        
        for i in range(n-1,-1,-1):
            while stk and temperatures[stk[-1]]<=temperatures[i]: #while the stack is not empty and the current temperature is greater than the temperature at the index on the top of the stack, 
                stk.pop()                                         #Pop the stack.
            if stk:
                ans[i] = stk[-1]-i                                #Set the value in the result array at the top index of the stack to the difference between the current index and the top index of the stack
            stk.append(i)                                         #Push the current index onto the stack
        return ans                                                #Return the result array.
    





#Approach:Monotonic Stack (Decreasing)
#TC:O(N)
#SC:O(N)

'''
We can also use a monotonically decreasing stack to find the next higher temperature.

We will use a stack to store the indices of the temperatures array. 
We iterate over the array, and for each temperature, we check whether the current temperature is greater than the temperature at the index on the top of the stack. 
If it is, we update the corresponding position in the result array and pop the index from the stack.
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stk = []    # a decreasing stack
        ans = [0]*n 
        
        for i,v in enumerate(temperatures):
            while stk and temperatures[stk[-1]]<v:
                index = stk.pop()
                ans[index]=i-index
            stk.append(i)
        return ans 
    



"""
i = 0 , v = 73
stk = [0]
ans = [0,0,0,0,0,0,0,0]

i = 1 , v =74
idx = 0
ans[idx] = i -idx 
ans[0] = 1-0 = 1 
stk = [1]

i = 2 , v = 75
idx = 1
ans[idx] = i - idx
ans[1] = 2-1 = 1
stk = [2]

i = 3 , v= 71

"""

