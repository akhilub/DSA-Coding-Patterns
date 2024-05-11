#Approach

#It is enough to traverse the array once ,intialize the two variables p1 and p2 to -1 and then
# traverse the array 

#When word1 is encountered its position is stored in p1 and if word2 is encountered its position is
#stored in p2.If p1,p2 are not -1 anymore then update the result

#TC:O(N)
#SC:O(1)

import math
class Solution:
    def shortestDistance(self,words,word1,word2):
        i = j = -1
        ans = math.inf # ans = len(words)
        for idx,ele in enumerate(words):
            if ele == word1:
                i = idx
            if ele == word2:
                j = idx
            if i!=-1 and j!=-1:
                ans = min(ans,abs(i-j))
        return ans

if __name__=="__main__":
     # Test case 1
    sol = Solution()

    #In Python, when you define a list literal, you cannot assign values to it later. List literals are immutable, which means their values cannot be changed once they are created.
    #words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], word1 = "fox", word2 = "dog"
    #This syntax is incorrect because you're trying to assign values to multiple variables in a single line. Python expects each assignment to be on a separate line.
    

    words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    word1 = "fox"
    word2 = "dog"

    expected_output = 5
    actual_output = sol.shortestDistance(words,word1,word2)
    
    print('Test Case1',expected_output==actual_output)

