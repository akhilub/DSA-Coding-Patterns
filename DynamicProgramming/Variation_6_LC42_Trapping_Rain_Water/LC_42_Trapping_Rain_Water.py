#Solution Logic
'''
We define `left[i]` as the height of the highest bar to the left of and including the position at index `i`, 
and `right[i]` as the height of the highest bar to the right of and including the position at index `i`. 
Therefore, the amount of rainwater that can be trapped at index `i` is `min(left[i],right[i])-height[i]`. 
We traverse the array to calculate `left[i]` and `right[i]`, and the final answer is 

n-1
∑  min( left[i], right[i] ) - height[i]
i=0

The time complexity is O(n), and the space complexity is O(n). Here, n is the length of the array.

'''

#Approach : Two Pointer + DP
#TC:O(n)
#SC:O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        #Intialization
        l = [height[0]] +  [0]*(n-1)
         
        r = [0]*(n-1) + [height[-1]]
        
        #Traverse & Compute
        for i in range(1,n):
            l[i] = max(l[i-1],height[i])
            r[n-1-i] = max(r[n-i],height[n-1-i])
            
        return sum(min(l[i],r[i]) - height[i] for i in range(n))


#Same Appraoch : Using Tilde(~) Operator , Easy to Visulize & write

'''
In python `~i` is equivalent to `-1-i`.
We can iterate over the list `height` from the end to the beginning


`~i` is used to access elements from the end of the list r in reverse order.
`~(i - 1)` allows us to correctly reference the previous element in the list when iterating in reverse.
'''


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        
        # Initialization
        l = [height[0]] + [0] * (n - 1)
        r = [0] * (n - 1) + [height[-1]]
        
        # Traverse & Compute
        for i in range(1, n):
            l[i] = max(l[i - 1], height[i])
            r[~i] = max(r[~(i - 1)], height[~i])

        
        return sum(min(l[i], r[i]) - height[i] for i in range(n))





#Another way of Writing Using zip
#TC:O(n)
#SC:O(n)


class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        
        left = [height[0]] * n
        right = [height[-1]] * n
        
        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])
            right[n - i - 1] = max(right[n - i], height[n - i - 1])
            
        return sum(min(l, r) - h for l, r, h in zip(left, right, height))
    
    
    
#Appraoch 2:
#TC:O(n)
#SC:O(1) 

# Not required my appraoch is more logical and easy to visulize
                
                
