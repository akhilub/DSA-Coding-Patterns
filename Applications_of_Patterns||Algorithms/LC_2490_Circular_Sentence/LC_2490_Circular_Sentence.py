#Approach1:Simulation
#TC:O(n)
#SC:O(n)

'''
We split the string into words by spaces, then check whether the last character of each word is equal to the first character of the next word. 
If they are not equal, return false. Otherwise, return true after traversing all the words.

The time complexity is O(n), 
and the space complexity is O(n). 
where n is the length of the string.
'''

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(' ')
        for i in range(len(words)):
            if words[i][0]!=words[i-1][-1]:
                return False
        return True
    

#Approach2:Simulation(Space Optimization)
#TC:O(n)
#SC:O(1)


'''
We can first check whether the first and last characters of the string are equal. 
If they are not equal, return false. 
Otherwise, traverse the string. If the current character is a space, check whether the previous character and the next character are equal. 
If they are not equal, return false. Otherwise, return true after traversing all the characters.

The time complexity is O(n), where n is the length of the string. 
The space complexity is O(1).
'''
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        for i in range(len(sentence)):
            if sentence[i]== ' ' and sentence[i-1]!=sentence[i+1]:
                return False
        return sentence[0]==sentence[-1]