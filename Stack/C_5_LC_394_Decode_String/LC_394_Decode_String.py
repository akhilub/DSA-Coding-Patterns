#Approach:Stack
# Time: O(∣ans∣)
# Space: O(∣ans∣)

'''
A recursive approach or using a stack are common solutions to this problem. 
I will provide a solution using a stack here:

1. A stack is used to keep track of the strings and numbers.
2. When a digit is encountered, it is accumulated in current_num.
3. On encountering `[`, the current context (current string and number) is saved onto the stack, and the current string and number are reset for a new context.
4. On encountering `]`, a previous context is popped from the stack, and the current string is updated by repeating it according to the popped number, then concatenating with the popped string.
5. If a non-digit, non-bracket character is encountered, it is added to the current string.
6. Finally, the current_string holds the decoded string.



Walk through the example s = "3[a2[bc]]"
1. Initialization: num_stk = [], str_stk = [], num = 0, res = ''.

2. Parsing s:
 - '3': num becomes 3.
 - '[': Push 3 into num_stk and '' into str_stk. Reset num and res.
 - 'a': res becomes 'a'.
 - '2': num becomes 2.
 -'[': Push 2 into num_stk and 'a' into str_stk. Reset num and res.
 - 'b' and 'c': res becomes 'bc'.
 - ']': Pop 2 from num_stk and 'a' from str_stk. Set res to 'a' + 'bc' * 2, which is 'abcbc'.
 - ']' again: Pop 3 from num_stk and '' (initial value) from str_stk. Set res to '' + 'abcbc' * 3, which is 'abcbcabcbcabcbc'.

3.Completion: No more characters in s. res = 'abcbcabcbcabcbc' is the final result.
'''

class Solution:
    def decodeString(self,s:str)->str:
        num_stk , str_stk = [] , []             # (repeatCount , prevStr)
        num , res = 0 , ''
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c == '[':
                num_stk.append(num)
                str_stk.append(res)
            elif c == ']':
                res = str_stk.pop() + res*num_stk.pop()
            else:
                res+=c 
                
        return res
    