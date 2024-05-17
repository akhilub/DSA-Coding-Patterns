#Approach:Two Pointer

class Solution:
    def reverseString(self, s: List[str]) -> None:
        l ,r = 0 ,len(s) -1
        while l <r:
            s[l] , s[r] = s[r] ,s[l]
            l+=1
            r-=1

class Solution:
    def reverseString(self,List[str]) -> None:
        s[:] == s[::-1]


#The code s[:] = s[::-1] works in this context because s is a list of characters, not a string. 
#Lists in Python are mutable, which means their contents can be changed. 
#When you use slicing with assignment on a list, you are modifying the elements of the list in place, which is allowed.