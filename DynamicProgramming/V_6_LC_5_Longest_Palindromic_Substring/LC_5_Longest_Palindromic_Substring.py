# NAIVE BRUTEFORCE ALGORITHM TO GET THE LONGEST PALINDROME SUBSTRING
# The first solution would be to bruteforce the substrings in O(N^2) time. And for each substring, we check if it is a palindrome which takes O(N) time. The overall time complexity is O(N^3).

# Please note that the array/string slicing in Python also takes O(N) time. Here, we store the left and right index of the longest palindrome substring.

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
# We can slightly improve the bruteforce, by reverse the inner check, and break once we have found a palindrome. No need to continue as the rest of the inner loop gives a shorter substring.
# Time complexity is still O(N^3).

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
# Checking palindrome substring is expensive but we can pre-compute this in O(N^2) using Dynamic Programming – which we can do it Top Down or Bottom Up.

# The Top Down is via Recursion and Memoization. It is based on the following observations. 
#Given f(i,j) represent substring `s[i:j+1]` from index i to index j inclusive is a palindrome

#             { 1 , if i==j i.e a single character is a palindrome
# f(i,j) =    {s[i]==s[j], if i+1==j   i.e two characters are palindrome 
#             {s[i]==s[j] and f(i+1,j-1)

# Recursion and memoziation implementation via the @cache keyword to remember the values that we have calculated. 
#Total N^2 states where N is the length of the string.


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


# The f function (Top Down DP) can replace the O(N) palindrome check direclty however it is still not fast enough as there is Recursion function call overhead. And we can improve this by Bottom Up Dynamic Programming which stores the F values in a two dimensional array.

#Write this in interviews
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        F = [[True]*n for _ in range(n)]
        for l in range(n-2,-1,-1):                          #filling the grid from bottom up
            for r in range(n-1,l,-1):
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