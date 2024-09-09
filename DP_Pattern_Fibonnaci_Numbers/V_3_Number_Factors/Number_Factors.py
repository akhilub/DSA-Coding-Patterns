#Approach : Functional Relationship

'''
Let f(n) represent the number of ways to write a number n as a sum of 1 , 3 and 4.

Consider one possible solution with n = x1 + x2 + x3 + … xn. 
If the last number is 1, then sum of the remaining numbers is n-1. So the number that ends with 1 is equal to f(n-1). 
Taking other cases into account where the last number is 3 and 4

We know its previous state would be n-1,n-3,n-4 thus the functional relationship would be

        {  1 , i==0
        {  1 , i==1
f(n)=   {  1 , i==2
        {  2 , i==3
        { f(n-1)+f(n-3)+f(n-4) , 4<=i<=n
'''

#Top-Down DP
class Solution:
  def countWays(self, n):
    def f(i,nb={}):
      if i ==0 or i==1 or i==2
        return 1
      if i==3:
        return 2
      if i in nb:
        return nb[i]
      nb[i] = f(i-1)+f(i-3)+f(i-4)
      return nb[i]
    return f(n)


#Bottom-Up DP
class Solution:
  def countWays(self, n):

    dp = [1,1,1,2]+[0]*(n-1)

    for i in range(4,n+1):
        dp[i] = dp[i-1]+dp[i-3]+dp[i-4]

    
    return dp[n]



#Bottom Up No Memory Dp

#we only store the previous 4 states to calculate the current dp[i] state.
# dp_i which store dp[i]
# dp_i_0 which store dp[i-4] 
# dp_i_1 which store dp[i-3]
# dp_i_2 which store dp[i-2]
# dp_i_3 which store dp[i-1]


class Solution:
  def countWays(self, n):
    #base cases
    if n==0 or n==1 or n==2:
        return 1
    if n==3:
        return 2

    #Intial States
    dp_i_0 = dp_i_1 = dp_i_2 = 1
    dp_i_3 = 2

    #Recursive states
    for i in range(4,n+1):
        dp_i = dp_i_3+dp_i_1+dp_i_0

        dp_i_0, dp_i_1, dp_i_2, dp_i_3 = dp_i_1, dp_i_2, dp_i_3, dp_i

    return dp_i