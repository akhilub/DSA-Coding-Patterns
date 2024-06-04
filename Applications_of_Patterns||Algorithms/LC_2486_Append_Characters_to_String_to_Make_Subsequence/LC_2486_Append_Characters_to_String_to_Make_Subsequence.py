# Approach:Two Pointers+Greedy 

# We define two pointers `i` and `j`, pointing to the first characters of strings `s` and `t` respectively. 
# We traverse string `t`, when s[i]!=s[j], we move pointer `i` forward until s[i] == s[j] or `i` reaches the end of string 
# If `i` reaches the end of string `s` , it means that the character t[j] in `t` cannot find the corresponding character in `s`, 
# so we return the remaining number of characters in `t`. 
# Otherwise, we move both pointers `i` and `j` forward and continue to traverse string `t`.

# The time complexity is O(m+n), and the space complexity is O(1). Where m and n are the lengths of strings s and t respectively.
class Solution:
    def appendCharacters(self,s,t):
        i , j = 0 , 0
        while i <len(s) and j < len(t):  #bounds for pointers i and j 
            if s[i]==s[j]:
                i , j = i+1 , j+1
            else:
                i+=1
        return len(t)-j