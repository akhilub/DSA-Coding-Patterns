#My Approach : HashTable

# We iterate over the nums array and keep one hashmap `seen` to check if we have seen that ele before
# Intially we haven't so add the ele to hashmap/dict/notebook
# Now if we have seen the ele it means we have found a pair so increment `pairCount` with the frequency of the seen element and increment the frequency of seen element

#TC : O(N)
#SC:

class Solution:
    def numIdenticalPairs(self,nums):
        pairCount = 0
        seen = {}
        for ele in nums:
            if num in seen:
                pairCount+=seen[num]
                seen[num]+=1
            else:
                seen[num]=1
        return pairCount


#Just another way of writing , see how it is condensed using the get() method of python dictionary
#the get() method is used to retrieve the freq/count of ele from the seen dictionary
#If `ele`is not in the dictionary, it will return the default value of 0. The count is then incremented by 1 and stored back into the `seen` dictionary.

class Solution:
    def numIdenticalPairs(self,nums):
        pairCount = 0
        seen = {}
        for ele in nums:
            pairCount+=seen.get(ele,0)
            seen[num]=seen.get(ele,0) + 1
        return pairCount



#Competative Programming Approach
from collections import Counter
class Solution:
    def numIdenticalPairs(self,nums):
        ans = 0
        cnt = Counter()
        for num in nums:
            ans+=cnt[num]
            cnt[num]+=1
        return ans
