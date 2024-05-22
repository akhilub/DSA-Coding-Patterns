#Approach 1:Use Language Built-in Functions

#We split the string into a list of strings by spaces, then reverse the list, and finally join the list into a string separated by spaces.

#Time complexity O(n), space complexity O(n), where n is the length of the string.


class Solution:
    def reverseWords(self,s):
        s = s.split() #split the sentence into list of words
        return ' '.join(s[::-1]) # join the list after reversing the list separated by space


#or using the reversed function which is equivalent to [::-1].
class Solution:
    def reverseWords(self,s):
        s = s.split() 
        return ' '.join(reversed(s))



# Python has some great string manipulation tools; starting from the innermost function:

# s.split() Takes a string and returns an Array of the non-whitespace parts. 'This is my string'.split() -> ['This', 'is', 'my', 'string']

# reversed(iter) Takes an iterable (list/array/set/...) and reverses it lazily. reversed['This', 'is', 'my', 'string']) -> ['string', 'my', 'is', 'This'] (note this would be after evaluating the lazy generator)

# " ".join(iter) Takes an iterable, such as a generator, and injects the char in between each element. In this case a space. ['string', 'my', 'is', 'This'] -> 'string my is This'

# Most of this is all abstracted away by the Python implementations of the algorithms leading to a lovely simple solution.

# Note: This can probably be sped up using the slice notation [::-1] on the split() over reversed, but is slightly less readable.




#For interviews
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        
        def reverseList(arr):
            l,r = 0,len(arr)-1
            while l<r:
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
                r-=1
            return arr
        
        return ' '.join(reverseList(s))


#Pythonic way same using lambda function
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        
        reverseList = lambda arr: arr[::-1]
        
        return ' '.join(reverseList(s))