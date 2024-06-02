#Approach 1: using a stack

#Traverse the bracket string `s`. When encountering a left bracket, push the current left bracket into the stack; when encountering a right bracket, pop the top element of the stack (if the stack is empty, directly return false), 
#and judge whether it matches. If it does not match, directly return false.


#At the end of the traversal, if the stack is empty, it means the bracket string is valid, return true; otherwise, return false.

# The time complexity is O(n), and the space complexity is O(n). Here, n is the length of the bracket string .

class Solution:                                                            #class Solution:  
    def isValid(self, s: str) -> bool:                                     #def isValid(self, s: str) -> bool:
        stack = []                                                              #stack = []
        for ch in s:                                                            #for ch in s:
            if ch in '({[':                                                         #if ch in '({[':
                stack.append(ch)                                                        #stack.append(ch)
            elif len(stack)==0 or not (stack.pop() + ch in ["()","{}","[]"]):           # elif not stack or not (stack.pop() + ch in ["()","{}","[]"]):
                return False                                                            #return False
            return len(stack)==0                                                    # return not stack