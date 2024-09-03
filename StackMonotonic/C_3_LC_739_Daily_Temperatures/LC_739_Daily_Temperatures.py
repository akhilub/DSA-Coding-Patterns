#Approach:Monotonic Stack (Increasing)
#TC:O(N)
#SC:O(N)


'''
We can use a monotonically increasing stack to find the next higher temperature.

We will use a stack to store the indices of the temperatures array. 
We iterate over the array, and for each temperature, we check whether the current temperature is greater than the temperature at the index on the top of the stack. 
If it is, we update the corresponding position in the result array and pop the index from the stack.
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