#My Approach
class Solution:
    def mergeAlternately(self,word1,word2):
        res , i , j = '' , 0 , 0
        while i <len(word1) and j <len(word2):
            res+= word1[i]+word2[j]
            i+=1
            j+=1
        #Remaining words from longer length
        res = word1[i:] + word2[j:]
        return res





#Competative Programming Approach

#We traverse the two strings word1 and word2 take out the characters one by one and append them
#to the result string.
#TC:O(N+M)
#SC:O(1)

#zip_longest()
#zip_longest() iterates up to the length of the longest iterator.
#and if one of the iterators runs out early, it gets replaced with None.

#zip()
#zip() iterates up to the length of the shortest iterator.
from itertools import zip_longest
class Solution:
    def mergeAlternately(self,word1,word2):
        return ''.join(a+b for a , b in zip_longest(word1,word2,fillvalue = ""))