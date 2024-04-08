#Notes:The chr() method is a built-in Python function that returns a string representing a character whose Unicode code point is the integer argument. 
#In simpler terms, it converts an integer to a character.

#For e.g chr(97) ---> a

#Approach 1
#Since the input string only contains the lowercase character we can add all the characters in a Counter(dict) or set and check if its length is 26.

#Using Counter
from collections import Counter
class Solution:
    def CheckIfPangram(self,sentence):
        ch = Counter(sentence)
        return len(ch)==26


#Using Set
class Solution:
    def CheckIfPangram(self,sentence):
        seen =set()
        for ch in sentence:
            seen.add(ch)
        return len(seen)==26

#Pythonic way
class Solution:
    def CheckifPangram(self,sentence):
        return len(set(sentence)) ==26


#Variations
#If all characters are allowed we can bruteforce -checking from 'a' to 'z' to see if they all are in the sentence
class Solution:
    def CheckIfPangram(self,sentence):
        for i in range(26):
            if chr(97+i) not in sentence:
                return False
        return True

#Checking character in string takes O(N) and thus solution takes O(26.N) time.But we can hash table (e.g Counter or Set) to achieve O(1) look up -O(N+26) time which is O(N)
class Solution:
    def CheckIfPangram(self,sentence):
        ch_set = set(sentence)
        for i in range(26):
            if chr(97+i) not in ch_set:
                return False
        return True

#Or we can explicitly count the number of occurences O(N+26) time
class Solution:
    def CheckIfPangram(self,sentence):
        ch_dict = Counter(sentence)
        for i in range(26):
            if ch_dict[chr(97+i)]==0:
                return False
        return True

#We can exit early if there are less than 26 characters
class Solution:
    def CheckIfPangram(self,sentence):
        if len(sentence)<26:
            return False
        ch_dict = Counter(sentence)
        for i in range(26):
            if ch_dict[chr(97+i)] == 0:
                return False
        return True


 






