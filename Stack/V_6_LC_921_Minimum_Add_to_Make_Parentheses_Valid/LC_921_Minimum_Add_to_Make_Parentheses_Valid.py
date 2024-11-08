#Approach1:Greedy+Stack
#TC:O(n)
#SC:O(n)


'''
This problem is a classic parenthesis matching problem, which can be solved using "Greedy + Stack".

Iterate through each character ch in the string s:

If ch is a left parenthesis, directly push ch into the stack;
If ch is a right parenthesis, at this point if the stack is not empty, and the top element of the stack is a left parenthesis, then pop the top element of the stack, indicating a successful match; otherwise, push 
ch into the stack.

After the iteration ends, the number of remaining elements in the stack is the number of parentheses that need to be added.

The time complexity is O(n), and the space complexity is O(n), where n is the length of the string s.
'''

class Solution:
    def minAddToMakeValid(self,s:int)->int:
        stk = []
        for ch in s:
            if ch==')' and stk and stk[-1]=='(':
                stk.pop() 
            else:
                stk.append(ch)
        return len(stk)
    
    
#Approach2:Greedy + Counting
#TC:O(n)
#SC:O(1)   
    
'''
Solution 1 uses a stack to implement parenthesis matching, but we can also directly implement it through counting.

Define a variable cnt to represent the current number of left parentheses to be matched, and a variable ans to record the answer. Initially, both variables are set to 0.

Iterate through each character ch in the string s:

If ch is a left parenthesis, increase the value of cnt by 1;
If ch is a right parenthesis, at this point if cnt>0, it means that there are left parentheses that can be matched, so decrease the value of cnt by 1; 
otherwise, it means that the current right parenthesis cannot be matched, so increase the value of ans by 1.
After the iteration ends, add the value of cnt to ans, which is the answer.

The time complexity is O(n), and the space complexity is O(1), where n is the length of the string s.
'''

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = cnt =0
        for ch in s:
            if ch == "(":
                cnt+=1
            elif cnt:
                cnt-=1
            else:
                ans+=1
        ans+=cnt
        return ans
    
    