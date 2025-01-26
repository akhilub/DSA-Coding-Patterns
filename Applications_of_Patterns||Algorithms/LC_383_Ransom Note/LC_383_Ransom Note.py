# 
# string.ascii_lowercase - ascii_lowercase is a useful tool that gives us a string containing all the lowercase letters from 'a' to 'z'
# string.ascii_uppercase - The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

'''
Syntax

import string
string.ascii_letters

'''
# ascii_letters - ascii_letters constant in the string module contains all the English letters from a to z. 
# These letters are in lowercase and uppercase as a single string.


#Pythonic Way- Using inbuilt libraries
import string
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt_r = Counter(ransomNote)
        cnt_m = Counter(magazine)
        
        return all(cnt_r[ch]<=cnt_m[ch] for ch in string.ascii_lowercase)
    

#Algorithm : Counting
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:   
        CH = 'abcdefghijklmnopqrstuvwxyz'
        
        # Count the occurrences of each character in ransomNote and magazine     
        cnt_m = {}
        for ch in magazine:
            cnt_m[ch]=cnt_m.get(ch,0)+1 

        #Add the character of ransomNote in magazine set if not present
        cnt_r = {}
        for ch in ransomNote:
            cnt_r[ch]=cnt_r.get(ch,0)+1
            cnt_m[ch]=cnt_m.get(ch,0)

        # Check if each character in ransomNote has enough occurrences in magazine
        return all(cnt_r[c]<=cnt_m[c] for c in CH if c in cnt_r and cnt_m)


#Optimised the above algo
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:   
        # Count the occurrences of each character in ransomNote and magazine     

        cnt_r = {}
        for ch in ransomNote:
            cnt_r[ch]=cnt_r.get(ch,0)+1
        
        cnt_m = {}
        for ch in magazine:
            cnt_m[ch]=cnt_m.get(ch,0)+1 

        # Check if each character in ransomNote has enough occurrences in magazine
        return all(cnt_r[c]<=cnt_m.get(c,0) for c in cnt_r)
    


#Approach: HashTable
#Algorithm 2
'''
We can use a hash table or an array `cnt` of length 26 to record the number of times each character appears in the string magazine. 
Then traverse the string ransomNote, for each character c in it, we decrease the number of c by 1 in `cnt`. 
If the number of c is less than 0 after the decrease, it means that the number of c in magazine is not enough, so it cannot be composed of ransomNote, just return false.

Otherwise, after the traversal, it means that each character in ransomNote can be found in magazine. Therefore, return true.

The time complexity is O(m+n), and the space complexity is O(C). Where 
m and n are the lengths of the strings ransomNote and magazine respectively; and C is the size of the character set, which is 26 in this question.
'''



class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt_m = {}
        for c in magazine:
            cnt_m[c]=cnt_m.get(c,0)+1 
        
        for ch in ransomNote:
            if ch in cnt_m and cnt_m[ch]>0:
                cnt_m[ch]-=1
            else:
                return False
        return True


#Using inbuilt libraries
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt_m = Counter(magazine)
        for ch in ransomNote:
            cnt_m[ch]-=1
            if cnt_m[ch]<0:
                return False
        return True
    

                