#Approach : Two Pointer 


# It should be noted that capital letters are counted, so there are ten letters in total.

# We write a isVowel function to determine whether the current character is a vowel,

# If both sides are vowels, then we exchange,
# If the one on the left is not, move one place to the right,
# If the one on the right is not, move one place to the left

# Time: O(n)
# Space: O(1)


class Solution:
    def reverseVowels(self,s):
        vowels = {"a",'e','i','o','u','A','E','I','O',"U"} #Define unique set of vowels
        chars = list(s)
        i , j = 0 ,len(chars)-1

        while i < j :
            if chars[i] not in vowels:
                i+=1
            elif chars[j] not in  vowels:
                j-=1
            else:
                chars[i] , chars[j] = chars[j] , chars[i] #Swap
                i , j = i+1 ,j-1                          #Do not forget to iterate the pointers
        return ''.join(chars)