#Approach : ITERATIVE DYNAMIC PROGRAMMING

#We define f(i) to represent the maximum sum of contigous subarray ending with element nums[i] at index i.
#At each index, we can choose to use previous subarray sum at f(i-1) or we can choose to ignore and start a new subarray with current single number nums[i]

# Core idea is  f(i) = max(f(i-1),0) + nums[i]   , 1=<i<n

# Initially, f[0] = nums[0] . The final answer we are looking for is  max(f[i]) for  0=<i< n  

class Solution:
    def maxSubarray(self,nums):
        res = curSum = 0
        for i in range(i,len(nums)):
            curSum = max(curSum,0) + nums[i]
            res = max(res,curSum)

        return ans

#TC: O(N)
#SC: O(1)




#Another way : Kaden's Algorithm
#We define dp[i] to represent the maximum sum of the continuous subarray ending with the element nums[i]. 
#Initially, dp [0] = nums [0 ]. The final answer we are looking for is max(dp) 

#Consider dp[i], where i>=1, its state transition equation is: dp[i] = max(nums[i], dp[i-1]+nums[i])

# which is also: f(i) = max(f(i-1),0) + nums[i]   , 1=<i<n

#Since dp[i] is only related to  dp[i-1], we can use a linear array to maintain the current value of dp[i] , and then perform state transition. 
#The answer is max(dp)

#TC: O(N)
#SC: O(N) since we are maintaing one array to capture the sum of subarray
class Solution:
    def maxSubarray(self,nums):
        dp = [0]* len(nums)

        dp[0] = nums[0]

        for i in range(1,len(nums)):
            dp[i] = max( nums[i],  dp[i-1] + nums[i])
        
        return max(dp)