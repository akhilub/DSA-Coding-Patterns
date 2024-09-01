#Approach:Prefix Sum + Hash Table
'''
According to the problem description, we can treat 0s in the array as -1. 
In this way, when encountering a 0, the prefix sum `s` will decrease by one, and when encountering a 
1, the prefix sum `s` will increase by one. 

Therefore, suppose the prefix sum `s` is equal at indices j and i, where j<i, 
then the subarray from index `j+1` to `i` has an equal number of 0s and 1s.

We use a hash table to store all prefix sums and their first occurrence indices. 
Initially, we map the prefix sum of 0 to -1.

As we iterate through the array, we calculate the prefix sum `s`. 
If `s` is already in the hash table, then we have found a subarray with a sum of 0, and its length is `i-d[s]`, where 
`d[s]` is the index where s first appeared in the hash table. 

If `s` is not in the hash table, we store `s` and its index `i` in the hash table.

The time complexity is O(n), and the space complexity is O(n), where 
n is the length of the array.
'''

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Dictionary to store the first occurrence of a particular count value
        d = {0,-1}                  # Initial count of 0 is assumed to occur at index -1
        s = 0                       # Initialize the count of 1's - 0's
        ans = 0                     # Variable to store the maximum length of the subarray found
        
        # Traverse through the given array
        for i , num in enumerate(nums):
            s +=1 if num else -1    # Increment count for 1 and decrement for 0               
            
            if s in d:              # If the count has been seen before, it means we have a subarray of equal 0's and 1's
                ans = max(ans,i-d[s]) # Calculate the length of this subarray
            else:                   
                d[s]=i              # Otherwise, store the first occurrence of this count
        return ans      
            
            
            
#Another way of writing the above approach

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0:-1}          #prefixSum to index mapping
        ans = s = 0         # s - prefixSum/count ,ans -maxLength
        
        for i in range(len(nums)):
            s += (1 if nums[i]==1 else -1)
            
            if s not in d:
                d[s]=i
            else:
                ans = max(ans,i-d[s])
                
        return ans        