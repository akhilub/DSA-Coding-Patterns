# Approach: Hash Table + Sorting

# 1. Traverse the string array, sort each string in character dictionary order to get a new string.
# 2. Use the new string as key and [str] as value, and store them in the hash table (HashMap<String, List<String>> ).
# 3. When encountering the same key during subsequent traversal, add it to the corresponding value .
# Take strs = ["eat", "tea", "tan", "ate", "nat", "bat"] as an example. At the end of
# the traversal, the state of the hash table is:


# ---------------------------------------
# |key     |   value                    |
#----------------------------------------   
# |"aet"   |   ["eat", "tea", "ate"]    |
# |"ant"   |   ["tan", "nat"]           |
# |"abt"   |   ["bat"]                  |
# ---------------------------------------

# Finally, return the value list of the hash table.
# The time complexity is O(n.k.logk), where n and k are the lengths of the string array and the maximum length of the string, respectively.


'''
>>> from collections import defaultdict
>>> d = defaultdict(list)
>>> d["a"]=1
>>> d["b"]=2
>>> d
defaultdict(<class 'list'>, {'a': 1, 'b': 2})
>>> d.values()
dict_values([1, 2])
>>> list(d.values())
[1, 2]

### sorted(str) will return a list of chars
>>> a = "sdfddxyz"
>>> sorted(a)
['d', 'd', 'd', 'f', 's', 'x', 'y', 'z']
>>> "".join(sorted(a))
'dddfsxyz'
'''


class Solution:
    def groupAnagram(self,strs):
        d = defaultdict(list)
        for s in strs:
            k = ''.join(sorted(s))
            d[k].append(s)
        return list(d.values())




















#Approach 2 : Counting

'''Write this in interviews'''

#TC:O(nm)
#SC:O(nm)
# m -> length of the longest word/string
# n -> length of the array


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for word in strs:
            key = [0] * 26
            for ch in word:
                key[ord(ch) - ord('a')] += 1
            mp[tuple(key)].append(word)
        return list(mp.values())