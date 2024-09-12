#Approach :Bottom Up DP
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