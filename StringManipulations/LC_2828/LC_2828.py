#Approach 1: Simulation

#We can iterate over each string in the array `words`, concatenate their first letters to form a new string `t` , 
#and then check if `t` is equal to `s` .

#The time complexity is O(n), and the space complexity is O(n). Here, n is the length of the array .

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        t = ''.join(w[0] for w in words)
        return t == s


#Approach 2: (Space Optimization)

#First, we check if the number of strings in `words` is equal to the length of `s`. If not, 
# `s` is definitely not an acronym of the first letters of `words`, and we directly return `False`.

#Then, we iterate over each character in `s`, checking if it is equal to the first letter of the corresponding string in `words`. If not, 
#`s`is definitely not an acronym of the first letters of `words`, and we directly return `False`.


#After the iteration, if we haven’t returned  `False`, then `s` is an acronym of the first letters of `words`, and we return `True`.

#The time complexity is O(n), where n is the length of the array `words`. The space complexity is O(1).


class Solution:
    def isAcronym(self,words,s):
        if len(words)!=len(s):
            return False
        
        for i in range(len(words)):
            if words[i][0]!=s[i]:
                return False

        return True




#Pythonic Way
class Solution:
    def isAcronym(self,words,s):
        return len(s)==len(words) and all(word[0]==ch for word,ch in zip(words,s))

