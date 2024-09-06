#Approach :HashTable

'''
We use a hash table d to store the nearest index of the number it has visited.
We traverse the array nums. For the current element numsli], if it exists in the hash table, and the difference between its index and the current index is no larger than k, then return true. Otherwise, we add the current element into the hash table.
After the traversal, return false •
The time complexity is O(n) and the space complexity is O(n). Here n is the length of array nums.
'''
#To vizulize create and see the hastable {1:0,2:1,3:2,1:4}
class Solution:
    def containsNearbyDuplicate(self,nums):
        d = {}
        for i ,v in enumerate(nums):
            if v in d and i - d[v]<=k:
                return True
            d[v]=i
        return False







