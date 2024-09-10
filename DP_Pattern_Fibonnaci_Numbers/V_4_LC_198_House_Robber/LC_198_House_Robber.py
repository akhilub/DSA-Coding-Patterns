#One thing is certain robber is always starting from house 1(i.e nums[0])

'''
Let F(i) denote the max numbers we can get up to i-th house, 
we know if we pick current i-th value, the total value would be F(i-2)+nums[i-1]
and if we don’t pick i-th value we have F(i-1).

Thus picking the max of two gives the value of F(n).

       { 0 , i==0
F(n) = { nums[0] , i==1
       { max(nums[0],nums[1]) , i==2
       { max(F(n-1),F(n-2)+nums[i-1]) , 2<i<=n
'''


#Start with the Bottom Up Tabulation Solution and then optimise it because input is in the form of array

# please note that dp[] has one extra element to handle zero house
# The trick is to make a dp array of nums.length() + 1 


# Dynamic Programming to solve, maintain a 1D array dp, where dp[i] represents the maximum value that can be grabbed in the [0, i] interval.
# For the current i, there are two mutually exclusive options for robbing and not robbing.
# Not robbing is dp[i-1] (equivalent to removing nums [i]), while robbing is the maximum value of [0, i-1]),
# Robbing is dp[i-2] + nums[i-1] (equivalent to removing nums [i-1] ).

# dp[i] = max(nums[i-1]+dp[i - 2], dp[i - 1])


#Bottom Up DP Tabulation
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums) # n is the no of house to be robbed
        if n==0:
            return 0
        if n==1:
            return nums[0]
        
        dp = [0]*(n+1)
        
        #Intial States
        dp[1]=nums[0]
        dp[2]= max(nums[0],nums[1])
        
        #Recursive states
        for i in range(2,n+1):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i-1])
        return dp[n]




#Bottom-Up (No Memory DP)

# Time: O(n)
# Space: O(1)

'''Write this in interviews'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0:
            return 0
        if n ==1:
            return nums[0]
        
        #Intial States when n>=2
        f0=0
        f1=nums[0]
        
        for i in range(2,n+1):
            fi = max(f1,f0+nums[i-1])
            f0,f1 = f1,fi
                
        return fi
    



#Top-Down DP

'''
Basically at any house `i` Robber have two options either to pick or skip

                                   f(i)
                                  /    \
                                 /      \    
                         H(i)+f(i-2)    f(i-1)
                           pick          skip
which boils down to    nums[i-1]+f(i-2)  f(i-1)

'''

#Write this in interviews
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def f(i , nb={}):
            if i==0:
                return 0
            if i==1:
                return nums[0]
            if i in nb:
                return nb[i]
            
            nb[i] = max(f(i-1),f(i-2)+nums[i-1])
            return nb[i]
        
        return f(n)
    
#Same Above Using Cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache #@lru_cache
        def dfs(i: int) -> int:
            if i ==0:
                return 0
            if i==1:
                return nums[0]
            return max(dfs(i - 1), dfs(i - 2)+nums[i-1] )
        return dfs(n)











# Greedy DP
class Solution:
    def rob(self, nums: List[int]) -> int:
        not_rob, rob = 0, nums[0]
        for num in nums[1:]:
            # must max check
            # eg. first robbed 99999, then following ones are just 3,3,3,3,3
            not_rob, rob = rob, max(num + not_rob, rob)
        return rob






















