#Approach :Naive Brute Force
#TC:O(n³)
#SC:O(n²)
#TLE








#Approach :Bottom Up DP
#TC:O(n²)
#SC:O(n²)

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        
        F = [[True]*n for _ in range(n)]
        
        for l in range(n-2,-1,-1):
            for r in range(l+1,n):
                F[l][r] = s[l]==s[r] and F[l+1][r-1]
                
        ans = 0
        for i in range(n):
            for j in range(n-1,i-1,-1):
                if F[i][j]: # F[i][j] tells if a substring from index i to j is palindrome or not
                    ans+=1
                    
        return ans
    








#Approach: Expand around the centers
#TC:O(n²)
#SC:O(1)


class Solution:
    def countSubstrings(self, s: str) -> int:
        def f(l: int, r: int) -> int:                           #f() aka extendPalindromes() aka expand() - a function that return the count of palindromic substring in a given string
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:         
                count += 1
                l -= 1
                r += 1
            return count

        ans , n = 0 , len(s)
        for i in range(n):
            ans += f(i, i)
            ans += f(i, i + 1)

        return ans






''' l>=0   OR   ~l  '''






#Approach: Enumerate(count one by one) Palindrome MidPoint DP 
#TC:O(n²)
#SC:O(1)


'''
Write this in interviews
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        ans, n = 0, len(s)
        for k in range(n*2 - 1):
            l, r = k//2, (k+1)//2
            while l>=0 and r < n and s[l] == s[r]:
                ans += 1
                l, r = l - 1, r + 1
        return ans














    
    
