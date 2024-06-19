

class Solution:
  def countWays(self, n):
    def f(i,nb={}):
        if i==0:
            return 1 # base case, we don't need to take any step, so there is only one way
        if i==1:
            return 1 # we can take one step to reach the end, and that is the only way
        if i==2:
            return 2 # we can take one step twice or jump two steps to reach at the top
        if i in nb:
            return nb[i]
        nb[i] = f(i-3)+f(i-2)+f(i-1)
        return nb[i]
    return f(n)





class Solution:
  def countWays(self, n):
    dp = [1,1,2] + [0]*(n-1)

    for i in range(3,n+1):
      dp[i] = dp[i-3]+dp[i-2]+dp[i-1]
    return dp[n]


class Solution:
  def countWays(self, n):
    if n==0:
        return 1
    if n==1:
        return 1
    if n==2:
        return 2

    f0,f1,f2 = 1,1,2
    for i in range(3,n+1):
        fi = f2+f1+f0
        f0,f1,f2 = f1,f2,fi
    return fi