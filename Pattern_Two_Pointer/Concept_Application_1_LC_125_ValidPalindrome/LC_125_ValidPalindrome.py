#Approach 1 :Two Pointer

# We use two pointer i  & j to point to the two ends of the string s and then loop through the process until i >= j:
#1)If s[i] is not a letter or a number, move the pointer i one step to the right and continue to the next loop
#2)If s[j] is not a letter or a number, move the pointer j one step to the left and continue to the next loop
#3)If the lowercase form of s[i] and lowercase form of s[j] are not equal return False
#4)Otherwise move the pointer i one step to the right and the pointer j one step closer to the left and continue to the next loop.


#At the end of the loop, return True
#TC:O(N)     SC: O(1)

class Solution:
    def validPalindrome(self,s):
        i , j = 0 , len(s)-1
        while i < j:
            #skip left if not alphanumeric
            if not s[i].isalnum():
                i+=1
            #skip right if not alphanumeric
            elif not s[j].isalnum():
                j-=1
            #convert lowercase to uppercase and compare
            elif s[i].lower() != s[j].lower():
                return False
            else:
            #move both pointers
                i , j = i + 1 ,j -1
        return True


#Approach 2 : Competative Programming

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() #convert all uppercase to lowercase
        s = re.sub(r'[^a-zA-Z0-9]', '', s) #remove all non-alphanumeric characters
        return s == s[::-1]