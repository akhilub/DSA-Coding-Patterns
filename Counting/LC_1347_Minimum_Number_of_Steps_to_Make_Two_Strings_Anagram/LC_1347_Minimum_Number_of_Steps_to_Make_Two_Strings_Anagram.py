#Approach:Counting

'''
We can use a hash table or an array cnt to count the occurrences of each character in the string s. Then, we traverse the string t. 
For each character, we decrement its count in cnt. 
If the decremented value is less than 0, it means that this character appears more times in the string t than in the string s. 
In this case, we need to replace this character and increment the answer by one.

After the traversal, we return the answer.

The time complexity is O(m+n), and the space complexity is O(∣Σ∣), where 
m and n are the lengths of the strings s and t, respectively, and 
∣Σ∣ is the size of the character set. In this problem, the character set consists of lowercase letters, so ∣Σ∣=26.
'''

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt = Counter(s)
        ans = 0
        for ch in t:
            if cnt[ch]>0:
                cnt[ch]-=1
            else:
                ans+=1
                
        return ans

'''
cnt = Counter(s)
    ||
    ||equivalent
    ||

cnt = defaultdict(int)
for c in s:
    cnt[c]+=1
'''

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt = Counter(s)
        ans = 0
        for ch in t:
            cnt[ch]-=1
            ans+= cnt[ch]<0
        return ans


'''
`ans += cnt[ch]<0`

This line takes two inputs: the current count of a character stored in cnt[ch] and adds either 0 or 1 to the running total ans. 

Here's how it works: When we check `cnt[ch]<0` , this creates a boolean expression that evaluates to either True (1) or False (0). If the count becomes negative, meaning we've found more instances of a character than we had in our original string, it evaluates to True (1) and adds 1 to our answer. 
If the count is 0 or positive, it evaluates to False (0) and effectively adds nothing.

'''

#Time : O(|s|+|t|)
#Space : O(26) = O(1)

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt = Counter(s)
        cnt.subtract(Counter(t))
        return sum(abs(value) for value in cnt.values())//2
    



#Using only HashMap no inbuilt functions 
#We are not in school anymore.This is real life and you are free to use the inbuilt libraries.There is no need to reinvent the wheel.


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        #frequency of s
        cnt_s = {}
        for c in s:
            cnt_s[c]= cnt_s.get(c,0)+1

        #frequency of t
        cnt_t = {}
        for c in t:
            cnt_t[c]= cnt_t.get(c,0)+1
        
        #count the characters if s's characters not present in t
        #and if present and frequency of s's characters are greater than that of t's then store their
        #frequency diff(coz only those need to replace from t)
        ans = 0
        for ch in cnt_s.keys():
            if ch in cnt_t:
                if cnt_s[ch]>cnt_t[ch]:
                    ans+=cnt_s[ch]-cnt_t[ch]
            else:
                ans+=cnt_s[ch]
        return ans
