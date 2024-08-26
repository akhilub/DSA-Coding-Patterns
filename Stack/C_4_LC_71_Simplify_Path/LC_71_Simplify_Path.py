#Approch: Stack
'''
We first split the path into a number of substrings split by '/'. 
Then, we traverse each substring and perform the following operations based on the content of the substring:

•If the substring is empty or '.', no operation is performed because '.' represents the current directory.

•If the substring is '..', the top element of the stack is popped, because '..' represents the parent directory.

•If the substring is other strings, the substring is pushed into the stack, 
because the substring represents the subdirectory of the current directory.

•Finally, we concatenate all the elements in the stack from the bottom to the top of the stack to form a string, 
which is the simplified canonical path.

The time complexity is O(n) and the space complexity is O(n), where n is the length of the path.
'''

class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        for str in path.split('/'):
            if str in ('','.'):
                continue
            if str =='..':
                if stk:
                    stk.pop()
            else:
                stk.append(str)
                
        return '/'+'/'.join(stk)
                    
                