#Approach: Counting

#A valid palindrome string can have at most one character that appears an odd number of times, and the rest of the characters appear an even number of times.

#Therefore, we can first traverse the string `s` count the number of times each character appears, and record it in an array or hash table cnt.


# Then, we traverse `cnt`, for each character c, if `cnt[c]` is even, then directly add `cnt[c]` to the answer `ans`; 
# if `cnt[c]` is odd, then add `cnt[c] -1` to `ans`

# if ans (computed length) equals the length of the original string i.e If they are equal, it means there were no characters with odd counts return ans
#Otherwise, we adds 1 to ans to account for a potential center character in the palindrome.


# The time complexity is O(n), and the space complexity is O(C). Here, n is the length of the string ; and C is the size of the character set, in this problem C =128


class Solution:
    def longestPalindrome(self, s: str) -> int:
        ch_cnt = Counter(s)
        ans=0
        for v in ch_cnt.values():
            if v & 1: #odd
                ans+=v-1
            else: #even
                ans+=v
                
        return ans if ans == len(s) else ans+1