# NAIVE BRUTEFORCE ALGORITHM TO GET THE LONGEST PALINDROME SUBSTRING
'''
The first solution would be to bruteforce the substrings in O(N^2) time. 
And for each substring, we check if it is a palindrome which takes O(N) time. 
The overall time complexity is O(N^3).

Please note that the array/string slicing in Python also takes O(N) time. Here, we store the left and right index of the longest palindrome substring.
'''
class Solution:
    def longestPalindrome(self,s):
        n = len(s)
        L=R=0                           #left and right index of longest palindrome
        for i in range(n):              #i is the left pointer
            for j in range(i,n):        #j is the right pointer
                c = s[i:j+1]            # current substring
                if c == c[::-1]:        # string palindrome check
                    if j-i>R-L:
                        L = i
                        R = j

        return s[L:R+1]


# OPTIMISED BRUTEFORCE ALGORITHM TO GET THE LONGEST PALINDROME SUBSTRING
'''
We can slightly improve the bruteforce, by reverse the inner check, and break once we have found a palindrome. 
No need to continue as the rest of the inner loop gives a shorter substring.
Time complexity is still O(N^3).
'''

class Solution:
    def longestPalindrome(self,s):
        n = len(s)
        L=R=0
        for i in range(n):                      #i is the left pointer
            for j in range(n-1,i-1,-1):         #j is the right pointer
                c = s[i:j+1]                    # current substring
                if c == c[::-1]:                # string palindrome check
                    if j-i>R-L:
                        L = i
                        R = j
                    break
        return s[L:R+1]


# DYNAMIC PROGRAMMING ALGORITHM TO CHECK IF A SUBSTRING IS A PALINDROME
'''
Checking palindrome substring is expensive but we can pre-compute this in O(N^2) using Dynamic Programming – which we can do it Top Down or Bottom Up.

The Top Down is via Recursion and Memoization. It is based on the following observations. 
Given f(i,j) represent substring `s[i:j+1]` from index i to index j inclusive is a palindrome

            { 1 , if i==j i.e a single character is a palindrome
f(i,j) =    {s[i]==s[j], if i+1==j   i.e two characters are palindrome 
            {s[i]==s[j] and f(i+1,j-1)

Recursion and memoziation implementation via the @cache keyword to remember the values that we have calculated. 
Total N^2 states where N is the length of the string.
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        #@cache                                             #causing MLE
        def f(i, j):
            if i == j:
                return True
            if i + 1 == j:
                return s[i] == s[j]
            return s[i] == s[j] and f(i + 1, j - 1)
        

        n = len(s)
        L = 0
        R = 0                                               #left and right index of longest palindrome
        for i in range(n):                                  #i is the left pointer 
            for j in range(n - 1, i - 1, -1):               #j is the right pointer 
                if f(i, j):                                 #current string palindromic check function
                    if j - i > R - L:                       #current length is greater than the longest length update the pointers for longest substring 
                        L = i
                        R = j
                    break
        return s[L:R+1]


# The f function (Top Down DP) can replace the O(N) palindrome check direclty however it is still not fast enough as there is Recursion function call overhead. 
# And we can improve this by Bottom Up Dynamic Programming which stores the F values in a two dimensional array.







#Bottom-Up
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        F = [[True]*n for _ in range(n)]
        for l in range(n-2,-1,-1):                          #filling the 2D array from bottom up
            for r in range(l+1,n):                          #moving index r from l+1 to n i.e traversing cols from left to right.Make grid 2d diagram and you will see.
                F[l][r] = s[l]==s[r] and F[l+1][r-1]
        
        L = 0
        R = 0                                               #left and right index of longest palindrome
        for i in range(n):                                  #i is the left pointer 
            for j in range(n - 1, i - 1, -1):               #j is the right pointer 
                if F[i][j]:                                 #current string palindromic check function
                    if j - i > R - L:                       #current length is greater than the longest length update the longest substring pointers
                        L = i
                        R = j
                    break
        return s[L:R+1]
        

# The time/space complexity is O(N^2) quadratic.





















'''Write this in interviews after telling intial brute force approach'''
#Best DP Solution
#Approach: Enumerate Palindrome MidPoint

'''
We can enumerate the midpoint of the palindrome, spread to both sides, and find the longest palindrome.

The time complexity is O(n²), and the space complexity is O(1). Here, 
n is the length of the string s.

'''



class Solution:
    def longestPalindrome(self, s: str) -> str:
        def f(l: int, r: int) -> int:                                        # f - a function to return the length of palindromic substring
            while l >= 0 and r < n and s[l] == s[r]:
                l, r = l - 1, r + 1
            return r - l - 1

        n = len(s)
        start, mx = 0, 1
        for i in range(n):
            a = f(i, i)
            b = f(i, i + 1)
            
            t = max(a, b)
            if mx < t:
                mx = t
                start = i - ((t - 1) >> 1)
        return s[start : start + mx]