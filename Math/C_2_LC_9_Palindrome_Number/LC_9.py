#Follow Up:Solution

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: return False
        y = self.reverse(x)
        return y==x
    
    def reverse(self,n):
        ans = 0
        while n!=0:
            r = n%10
            ans =ans*10 + r
            n=n//10
        return ans