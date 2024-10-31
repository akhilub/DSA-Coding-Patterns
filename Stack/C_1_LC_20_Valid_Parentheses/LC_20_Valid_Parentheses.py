#Approach:Stack

#Write this in interviews

'''
To solve this problem, we can use a stack. We'll iterate through each character in the string. 

If we encounter an opening bracket, we'll push it onto the stack. 
If we encounter a closing bracket,
    •we'll check if the stack is empty or 
    •if the top of the stack and the poped top element from the stack doesn't match the corresponding opening bracket. 
    
If either condition is true, we return false.

After processing all characters, we check if the stack is empty. If it is, all brackets were properly closed, and we return true. 
If not, there are unmatched opening brackets, so we return false.

The time complexity of this solution is O(n), where n is the length of the input string. We iterate through each character once, and stack operations (push and pop) are O(1)
'''



class Solution:
    def isValid(self, s: str) -> bool:
        stack = []                                          # Stack to keep track of opening brackets
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            elif len(stack)==0 or (stack.pop()+ch) not in ["()","{}","[]"]:
                return False
            
        return len(stack)==0










"""
len(stack)==0

    ||
equivalent
    ||
    
not stack

"""



"""

not (stack.pop() + ch in ["()","{}","[]"])

                    ||
                equivalent
                    ||
                    
(stack.pop()+ch) not in ["()","{}","[]"]

"""

























#Approach: Using a stack
#See how to use inbuilt language tools
'''
Traverse the bracket string `s`. 
•When encountering a left bracket, push the current left bracket into the stack; 
•When encountering a right bracket, pop the top element of the stack (if the stack is empty, directly return false), 
and judge whether it matches. If it does not match, directly return false.

At the end of the traversal, 
•if the stack is empty, it means the bracket string is valid, return true; 
otherwise, return false.

The time complexity is O(n), and the space complexity is O(n). 
Here, n is the length of the bracket string .
'''

class Solution:                                                            
    def isValid(self, s: str) -> bool:                                     
        stack = []
        valid = ["()","{}","[]"]         # valid = {'()', '[]', '{}'}
                                                                      
        for ch in s:                                                           
            if ch in '({[':                                                        
                stack.append(ch)                                                        
            elif not stack or not (stack.pop() + ch in valid):          
                return False                                                            
        return not stack                                                 




