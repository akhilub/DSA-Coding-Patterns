#Approach:Modified Binary Search

#Python ord()
#The ord() function returns an integer representing the Unicode character.

#print(ord('5'))    # 53
#print(ord('A'))    # 65
#print(ord('$'))    # 36

class Solution:
    def searchNextLetters(self,letters,target):
        l = 0 
        r = len(letters)
        while l < r: #see when left <right , assign mid to right
            m = (l+r) // 2
            if ord(letter[m]) > ord(target):
                r = m
            else: #ord(letter[m]) <= ord(target)
                l = m+1
        # since the loop is running until 'left < right', so at the end of the while loop, 
        # 'left == right+1'
        return letters[l % len(letters)] #because the array is considered circular.







#competative Programming
import bisect
class Solution:
  def searchNextLetters(self, letters: List[str], target: str) -> str:
    l = bisect.bisect_right(range(len(letters)), target, key=lambda m: letters[m])

    return letters[l % len(letters)]