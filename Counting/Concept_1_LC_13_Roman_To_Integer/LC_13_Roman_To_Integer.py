# zip does not produce combinations, it iterates over two objects and creates pairs.

# a = 1, 2, 3, 4
# b = 2, 3, 4, 5

# zip(a, b)  # (1, 2), (2, 3), (3, 4), (4, 5)
# If one iterable is shorter than another, then zip gives an iterable that is the length of the shorter.

# a = 1, 2, 3
# b = 2, 3, 4, 5

# zip(a, b)  # (1, 2), (2, 3), (3, 4)

#Approach1:
#TC:O(N)
#SC:O(128) = O(1)
class Solution:
    def romanToInt(self,s):
        ans = 0
        roman = {"I":1,"V":5,"X":10,"L":50,'C':100,'D':500,'M':1000}

        for a , b in zip(s,s[1:]):
            if roman[a] < roman[b]:
                ans -= roman[a]
            else:
                ans+ roman[a]
        return ans + roman[s[-1]]


#Another way of writing
#If current roman value is less than the next roman character, we need to deduct the value, otherwise, we add it. For example, “IV” is -I+V=4 and “VI” is V+I=6

class Solution:
    def romanToInt(self,s):
        ans = 0 
        data = {"I":1,"V":5,"X":10,"L":50,'C':100,'D':500,'M':1000}
        n = len(s)
        for i in range(n-1):
            if data[s[i]] < data[s[i+1]]: # #current character value is less than the next one then subtract the value from hashmap
                ans-=data[s[i]]
            else: #current character is greater than the next one then add the value from hashmap
                ans+=data[s[i]]
        return ans + data[s[-1]]