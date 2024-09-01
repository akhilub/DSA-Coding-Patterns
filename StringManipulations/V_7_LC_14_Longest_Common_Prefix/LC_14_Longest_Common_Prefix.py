#Approach: Two Pointers Traversal

# TC: O(∣strs[0]∣⋅∣strs∣)
# SC: O(1)

'''
Character Comparison

We use the first string `strs[0]` as a benchmark, and compare whether the 
`i-th` character of the subsequent strings is the same as the `i-th` character of `strs[0]`. 

•If they are the same, we continue to compare the next character. Otherwise, we return the first `i` characters of `strs[0]`.

•If the traversal ends, it means that the first `i` characters of all strings are the same, and we return strs[0].

The time complexity is O(n x m), where m are the length of the string array and the minimum length of the strings, respectively. 
The space complexity is O(1).

'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for j in range(1,len(strs)):
                if i==len(strs[j]) or strs[j][i]!=strs[0][i]:
                    return strs[0][:i]
                
        return strs[0]
    

#Better way of writing the same below code
#Easy to write in interviews

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s1 = strs[0]
        for i in range(len(s1)):
            for s in strs[1:]:
                if len(s)<=i or s[i]!=s1[i]:     # len(s)<=i condition mean any string 's' is within the bound
                    return s1[:i]    
        return s1
                
                

        