# Optimised One Pass

# Time: O(n)
# Space: O(n)


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []                                      # To capture unpaired '(' indices
        chars = list(s)
        for i , c in enumerate(s):
            if c =='(':
                stack.append(i)                         # Record the unpaired '(' index.
            elif c ==')':
                if stack:
                    stack.pop()                         # Find a pair
                else:
                    char[i] = '*'                       # Mark the unpaired ')' as '*'.
        
        # Mark the unpaired '(' as '*'.
        while stack:
            chars[stack.pop()] = '*'
            
        return ''.join(chars).replace('*','')