#Approach 1:

#1)Create a HashMap 
#2)Iterate the dictionary and check for the ceiling (majority element count)
import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_dict = Counter(nums)
        n = math.ceil(len(nums)/2)
        for key , value in maj_dict.items():
            if value >= n:
                return key


#Appeoach 2:
#Problem is asking about Boyers Moore Algorithm which is as follows

#Moore Voting Algorithm

#The basic steps of the Moore voting algorithm are as follows:

#Initialize the element m and initialize the counter cnt=0. Then, for each element x in the input list:

#1) If cnt = 0  ,then m = x  and cnt =1;
#2) Otherwise, if m=x, then cnt = cnt+1, otherwise cnt = cnt-1

# In general, the Moore voting algorithm requires two passes over the input list. In the first pass, we generate the candidate value m
# and if there is a majority, the candidate value is the majority value. 
# In the second pass, we simply compute the frequency of the candidate value to confirm whether it is the majority value. Since this problem has clearly stated that there is a majority value, we can directly return m
# after the first pass, without the need for a second pass to confirm whether it is the majority value.

# The time complexity is O(n), where n is the length of the array nums
# The space complexity is O(1).

class Solution:
    def majorityElement(self,nums):
        cnt = m = 0
        for x in nums:
            if cnt ==0:
                m,cnt =x,1
            else:
                cnt+=1 if m==x else cnt-=1
        return m


