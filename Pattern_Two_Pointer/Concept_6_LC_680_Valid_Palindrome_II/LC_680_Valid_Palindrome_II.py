#Approach 1: Two Pointer (Basic)
#Stick with this for interview easy to write and explain
#Write Structured Code, Follow Top Down Approach

'''
We use two pointers to point to the left and right ends of the string, respectively. 
Each time, we check whether the characters pointed to by the two pointers are the same. 

•If they are not the same, we check whether the string is a palindrome after deleting the character corresponding to the left pointer, 
or we check whether the string is a palindrome after deleting the character corresponding to the right pointer. 

•If the characters pointed to by the two pointers are the same, we move both pointers towards the middle by one position, until the two pointers meet.

If we have not encountered a situation where the characters pointed to by the pointers are different by the end of the traversal, 
then the string itself is a palindrome, and we return true.

The time complexity is O(n), where n is the length of the string `s`
The space complexity is O(1).

'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l , r =  0 , len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return self.checkPalindrome(s,l,r-1) or self.checkPalindrome(s,l+1,r)
            l , r = l+1,r-1
            
        return True
    
    # function to check whether a substring of `s` (between indices L and R, inclusive) is a palindrome.
    def checkPalindrome(self,s,L:int,R:int)->bool:
        while L<R:
            if s[L]!=s[R]:
                return False
            L , R = L+1, R-1
        return True
                
































































#Approch 2: Two Pointers (Advanced)
#Same Logic Using For Loop & Tilde Operator
#Do not go with this because this approach is not extendable
'''
Python Tilde(~) Operator

`~i = -1-i`

'''

class Solution:
  def validPalindrome(self, s: str) -> bool:
    # function to check whether a substring of `s` (between indices L and R, inclusive) is a palindrome.
    def checkPalindrome(L:int,R:int)->bool:     
        return all(s[i]==s[R-i+L] for i in range(L,(L+R)//2+1))

    n = len(s)
    for i in range(n//2):
        if s[i]!=s[~i]:
            return checkPalindrome(i+1,n-1-i) or checkPalindrome(i,(n-1-i)-1)
    return True
