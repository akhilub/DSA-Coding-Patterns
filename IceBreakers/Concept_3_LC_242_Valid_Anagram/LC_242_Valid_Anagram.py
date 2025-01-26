#Approach 1: Using Sorting
# We can sort both the strings ,and the anagrams will be exactly the same after sorted.
# In Python we can sort the strings directly, however we can converted to list and then join
#TC: O(NlogN)

class Solution:
    def validAnagram(self,s,t):
        if len(s)!=len(t):
            return False
        
        s = "".join(sorted(s))
        t = "".join(sorted(t))
        return s==t

# Approach 2: Using HashTable
#Full Approach if using built in functions are not allowed to be used
# In Python the dictionary is annotated in curly braces.If you want to access a item in the
#dictionary , the key must be existant ,otherwise an exception will be raised.We can count two 
#strings and put their letters and frequencies in two maps and then we can compare both

#TC:O(N)
#SC:O(N)

class Solution:
    def validAnagram(self,s,t):
        s_dict ,t_dict= {},{}
        #counting the letters for s
        for i in s:
            if i in s_dict:
                s_dict[i]+=1
            else:
                s_dict[i]=1

        #counting the letters for t
        for i in t:
            if i in t_dict:
                t_dict[i]+=1
            else:
                t_dict[i]=1

        #Different size cant be anagram
        if len(s_dict)!=len(t_dict):
            return False

        #comparing two dictionaries
        for i in s_dict.keys():
            if i not in t_dict or s_dict[i]!=t_dict[i]:
                return False
        
        for i in t_dict.keys():
            if i not in s_dict or s_dict[i]!=t_dict[i]:
                return False

        return True

#To check if the two dictionaries are simply equal, we can simply use the == operator
#Thus the above function reduced to


class Solution:
    def validAnagram(self,s,t):
        s_dict ,t_dict= {},{}
        #counting the letters for s
        for i in s:
            if i in s_dict:
                s_dict[i]+=1
            else:
                s_dict[i]=1

        #counting the letters for t
        for i in t:
            if i in t_dict:
                t_dict[i]+=1
            else:
                t_dict[i]=1

        #comparing two dictionaries
        return s_dict == t_dict

#Also with the usage of defaultdict we dont need to check if a key is existent before the 
#we update the item , just make sure to specify a default type/constructor- which is int type:

from collections import defaultdict
class Solution:
    def validAnagram(self,s,t):
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        #count in s_dict
        for i in s_dict:
            s_dict[i]+=1
        #count in t_dict

        for i in t_dict:
            t_dict[i]+=1

        return s_dict == t_dict


#Now can we do better ? Yes in Python we can count the items using Counter object
from collections import Counter
class Solution:
    def validAnagram(self,s,t):
        return Counter(s)==Counter(t)









#Standard Approach
#1) Compare the character count of both the string by creating a hashset/hashtable
#2) Check for the edge case like when len of both the string are not equal return False

# Time: O(n)
# Space:O(26)=O(1)
from collections import Counter
class Solution:
    def validAnagram(self,s,t):
        if len(s)!=len(t):
            return False
        
        count = Counter(s)
        count.subtract(Counter(t))

        return all(freq == 0 for freq in count.values())


#Note:
#1)The all(iterable) function returns True , if all items in iterable(list,set,tuple,dictionary) are True ,other it will return False
#2)When used on dictionary the all() function checks if the keys are True and not the values    