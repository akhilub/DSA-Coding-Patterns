#Approach: HashSet

#To solve this problem in O(n) time, we can use a HashSet to store all the numbers in the array. This will allow us to check if a number is present in the set in O(1) time.

#We'll iterate through each number in the array. For each number, we'll check if its previous consecutive number (num - 1) is in the set. If it is, that means this number is the start of a sequence.

#We'll then keep incrementing the number and checking if the next consecutive number is in the set. We'll do this until we find a number that is not in the set, which marks the end of the sequence.

#We'll update the longest sequence length if the current sequence length is greater.

#The time complexity of this solution is O(n) because we iterate through the array once, and each HashSet operation takes O(1) time on average.

#Space Complexity is O(m) because we have created a hashset to store the unique element of array in worst case


class Sequence:
    def longestConsecutive(self,nums):
        if not nums:
            return 0
        
        ans = 0   #length of longest consecutive element sequence
        seen = set(nums)
        for num in nums:
            #Check if it is the start of a sequence
            if num-1 in seen:
                continue 
            length = 0 #current length of the sequence

            #Expand the sequence
            while num in seen:
                num+=1
                length+=1
            
            #update the maximum length
            ans = max(ans,length)

        return ans
